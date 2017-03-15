#!/usr/bin/env python
# -*- coding: utf-8 -*- 

from locust import HttpLocust, TaskSet, task

def webPageLoad(l):
    print(l);
    r = l.client.get("/", verify=False)


class UserBehavior(TaskSet):
    tasks = {webPageLoad: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 30000