---
title: Quartz
---

# Quartz とは？

ジョブスケジューリングを行うためのライブラリ。

# 概要

`Job`と`Trigger`を`Scheduler`に登録することで、処理のスケジューリングが行われる。

- `Scheduler`：ジョブを実行する本体
- `Job`：指定時間に実行したい処理を定義
- `Trigger`：スケジュールを定義

# pom.xml の設定

```xml
<!-- https://mvnrepository.com/artifact/org.quartz-scheduler/quartz -->
<dependency>
    <groupId>org.quartz-scheduler</groupId>
    <artifactId>quartz</artifactId>
    <version>2.3.0</version>
</dependency>
```

# ジョブの定義・実行

```java
import org.quartz.Job;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

public class PrintJob implements Job {
    public PrintJob() {}

    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println(Thread.currentThread().getName() + " : " + getClass().getSimpleName() + " started.");
        System.out.println(Thread.currentThread().getName() + " : " + getClass().getSimpleName() + " finished.");
    }
}
```

```java
import org.quartz.Job;
import org.quartz.JobExecutionContext;
import org.quartz.JobExecutionException;

/**
 * sleep しつつ複数回 print を実行する
 */
public class LongPrintJob implements Job {
    public LongPrintJob() {}

    private static final int intervalMillis = 500;

    public void execute(JobExecutionContext context) throws JobExecutionException {
        System.out.println(Thread.currentThread().getName() + " : " + getClass().getSimpleName() + " started.");
        try {
            Thread.sleep(intervalMillis);
        } catch (InterruptedException e) {
            throw new RuntimeException(e);
        }
        System.out.println(Thread.currentThread().getName() + " : " + getClass().getSimpleName() + " finished.");
    }
}
```


```java
import org.quartz.*;
import org.quartz.impl.StdSchedulerFactory;

import static org.quartz.SimpleScheduleBuilder.simpleSchedule;

public class QuartzTrialMain {
    public static void main(String[] args) {
        executePrintJob();
        executeLongPrintJob();
    }

    /**
     * シンプルな例
     */
    private static void executePrintJob() {
        JobDetail job = JobBuilder.newJob(PrintJob.class)
                .withIdentity("job1", "group1")
                .build();
        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("trigger1", "group1")
                .startNow()
                .withSchedule(simpleSchedule()
                        .withIntervalInMilliseconds(1000)
                        .repeatForever()
                ).build();
        Scheduler scheduler = null;
        try {
            scheduler = StdSchedulerFactory.getDefaultScheduler();
            scheduler.scheduleJob(job, trigger);
            scheduler.start();
        } catch (SchedulerException e) {
            throw new RuntimeException(e);
        }

        System.out.println("##### " + job.getJobClass().getSimpleName() + " started #####");

        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        try {
            scheduler.shutdown();
        } catch (SchedulerException e) {
            throw new RuntimeException(e);
        }

        System.out.println("##### " + job.getJobClass().getSimpleName() + " finished #####");
    }

    /**
     * 次のジョブ開始までに前のジョブが終わらないケース（ジョブが重複する）
     */
    private static void executeLongPrintJob() {
        JobDetail job = JobBuilder.newJob(LongPrintJob.class)
                .withIdentity("job1", "group1")
                .build();
        Trigger trigger = TriggerBuilder.newTrigger()
                .withIdentity("trigger1", "group1")
                .startNow()
                .withSchedule(simpleSchedule()
                        .withIntervalInMilliseconds(200)
                        .repeatForever()
                ).build();
        Scheduler scheduler = null;
        try {
            scheduler = StdSchedulerFactory.getDefaultScheduler();
            scheduler.scheduleJob(job, trigger);
            scheduler.start();
        } catch (SchedulerException e) {
            throw new RuntimeException(e);
        }

        System.out.println("##### " + job.getJobClass().getSimpleName() + " started #####");

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        try {
            scheduler.shutdown();
        } catch (SchedulerException e) {
            throw new RuntimeException(e);
        }

        System.out.println("##### " + job.getJobClass().getSimpleName() + " finished #####");
    }
}
```
