+++
type = "question"
title = "GPSMaster and java v9"
description = '''I am not sure this is the correct place to ask this question but I cannot find any other resource. I tried to start GPSMaster with the command line command java -jar GpsMaster_0.63.00.jar I get the following error Exception in thread &quot;main&quot; java.lang.NoClassDefFoundError: javax/xml/bind/JAXBExceptio...'''
date = "2017-11-10T19:29:00Z"
lastmod = "2017-11-12T08:48:00Z"
weight = 60541
keywords = [ "java_v9", "gpsmaster" ]
aliases = [ "/questions/60541" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [GPSMaster and java v9](/questions/60541/gpsmaster-and-java-v9)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60541-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60541-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-60541-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am not sure this is the correct place to ask this question but I cannot find any other resource.</p>
<p>I tried to start GPSMaster with the command line command java -jar GpsMaster_0.63.00.jar</p>
<p>I get the following error Exception in thread "main" java.lang.NoClassDefFoundError: javax/xml/bind/JAXBException at java.base/java.lang.Class.forName0(Native Method) at java.base/java.lang.Class.forName(Unknown Source) at org.eclipse.jdt.internal.jarinjarloader.JarRsrcLoader.main(JarRsrcLoader.java:56) Caused by: java.lang.ClassNotFoundException: javax.xml.bind.JAXBException at java.base/java.net.URLClassLoader.findClass(Unknown Source) at java.base/java.lang.ClassLoader.loadClass(Unknown Source) at java.base/java.lang.ClassLoader.loadClass(Unknown Source) ... 3 more</p>
<p>I have also tried "C:\Program Files\Java\jre-9.0.1\bin\java" -jar GpsMaster_0.63.00.jar and get the same error</p>
<p>Java has been updated to v9 which is 64-bit only.</p>
<p>Am I doing something wrong (I cannot find any documentation on how to start GPSMaster.jar) or does GPSMaster need modifying for java v9?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-java_v9" rel="tag" title="see questions tagged &#39;java_v9&#39;">java_v9</span> <span class="post-tag tag-link-gpsmaster" rel="tag" title="see questions tagged &#39;gpsmaster&#39;">gpsmaster</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Nov '17, 19:29</strong></p>
<img src="https://secure.gravatar.com/avatar/8d7bf9e6b59c24278c878dd0eea2e009?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ElsieBB&#39;s gravatar image" />
<p><span>ElsieBB</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ElsieBB has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-60541" class="comments-container">
<span id="60547"></span>
<div id="comment-60547" class="comment">
<div id="post-60547-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I have an imac and java 8 and GpsMaster_0.63.00.jar works fine so installing java 8 might be easiest temporary solution for now.<br />
There is a developer contact listed near the end of this page... <a href="http://wiki.openstreetmap.org/wiki/GpsMaster">http://wiki.openstreetmap.org/wiki/GpsMaster</a></p>
</div>
<div id="comment-60547-info" class="comment-info">
<span class="comment-age">(11 Nov '17, 12:19)</span> <span class="comment-user userinfo">nevw</span>
</div>
</div>
</div>
<div id="comment-tools-60541" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60541-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="60568"></span>

<div id="answer-container-60568" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-60568-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-60568-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-60568-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Thank you. I reinstalled java v8 in another directory and GPSMaster runs when I use that.</p>
<p>Having now searched for some of the errors, other software has similar problems.</p>
<p>There are significant changes between v8 and v9 (and even more for the future v10) which mean many applications are going to need to be revised.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>12 Nov '17, 08:48</strong></p>
<img src="https://secure.gravatar.com/avatar/8d7bf9e6b59c24278c878dd0eea2e009?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ElsieBB&#39;s gravatar image" />
<p><span>ElsieBB</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ElsieBB has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-60568" class="comments-container">
&#10;</div>
<div id="comment-tools-60568" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-60568-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

