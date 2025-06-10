+++
type = "question"
title = "Nominatim Setup - Failed to Open Stream"
description = '''I&#x27;m trying to get nominatim up and running but am running into some problems. Here are the last few lines from my execution. Anyone run into this problem? Did I mess up the build steps?  Loading word list SET SET SET SET SET SET SET SET CREATE TABLE  count  -------  1772 (1 row)   count  -------  4 ...'''
date = "2013-10-28T14:29:00Z"
lastmod = "2013-11-05T14:21:00Z"
weight = 27578
keywords = [ "setup", "nominatim" ]
aliases = [ "/questions/27578" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Nominatim Setup - Failed to Open Stream](/questions/27578/nominatim-setup-failed-to-open-stream)

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
<span id="post-27578-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27578-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27578-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to get nominatim up and running but am running into some problems. Here are the last few lines from my execution. Anyone run into this problem? Did I mess up the build steps?</p>
<pre><code>    Loading word list
SET
SET
SET
SET
SET
SET
SET
SET
CREATE TABLE
 count 
-------
  1772
(1 row)
&#10; count 
-------
     4
(1 row)
&#10; count 
-------
    45
(1 row)
&#10;UPDATE 469
DROP TABLE
Load Data
........
Reanalysing database...
NOTICE:   no notnull values, invalid stats
ANALYZE
Oct 28, 2013 9:59:04 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Osmosis Version 0.40.1
Oct 28, 2013 9:59:04 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Preparing pipeline.
Oct 28, 2013 9:59:04 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Launching pipeline execution.
Oct 28, 2013 9:59:04 AM org.openstreetmap.osmosis.core.Osmosis run
INFO: Pipeline executing, waiting for completion.
Oct 28, 2013 9:59:04 AM org.openstreetmap.osmosis.core.pipeline.common.ActiveTaskManager waitForCompletion
SEVERE: Thread for task 1-read-replication-interval-init failed
org.openstreetmap.osmosis.core.OsmosisRuntimeException: Unable to open lock file /home/spbryfczynski/Documents/geocode/Nominatim/settings/download.lock.
        at org.openstreetmap.osmosis.core.util.FileBasedLock.initialize(FileBasedLock.java:53)
        at org.openstreetmap.osmosis.core.util.FileBasedLock.lock(FileBasedLock.java:68)
        at org.openstreetmap.osmosis.replication.v0_6.ReplicationDownloaderInitializer.run(ReplicationDownloaderInitializer.java:72)
        at java.lang.Thread.run(Thread.java:724)
&#10;Oct 28, 2013 9:59:04 AM org.openstreetmap.osmosis.core.Osmosis main
SEVERE: Execution aborted.
org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed.
        at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146)
        at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92)
        at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37)
        at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
        at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.lang.reflect.Method.invoke(Method.java:606)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:328)
        at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238)
        at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:408)
        at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:351)
        at org.codehaus.classworlds.Launcher.main(Launcher.java:31)
&#10;sed: can&#39;t read /home/spbryfczynski/Documents/geocode/Nominatim/settings/configuration.txt: No such file or directory
sed: can&#39;t read /home/spbryfczynski/Documents/geocode/Nominatim/settings/configuration.txt: No such file or directory
PHP Warning:  file_get_contents(http://www.openstreetmap.org/api/0.6/node/2506472169/1): failed to open stream: Connection timed out in /home/spbryfczynski/Documents/geocode/Nominatim/utils/setup.php on line 540
PHP Notice:  Undefined offset: 1 in /home/spbryfczynski/Documents/geocode/Nominatim/utils/setup.php on line 542
PHP Warning:  file_get_contents(http://planet.openstreetmap.org/replication/minute/?C=M;O=D): failed to open stream: Connection timed out in /home/spbryfczynski/Documents/geocode/Nominatim/utils/setup.php on line 546
PHP Notice:  Undefined variable: aRepMatch in /home/spbryfczynski/Documents/geocode/Nominatim/utils/setup.php on line 558</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-setup" rel="tag" title="see questions tagged &#39;setup&#39;">setup</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Oct '13, 14:29</strong></p>
<img src="https://secure.gravatar.com/avatar/cedcf7f648595f10a2eff219e1b94922?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbryfcz&#39;s gravatar image" />
<p><span>sbryfcz</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbryfcz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27578" class="comments-container">
&#10;</div>
<div id="comment-tools-27578" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27578-form-container" class="comment-form-container">
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

2 Answers:

</div>

</div>

<span id="27603"></span>

<div id="answer-container-27603" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27603-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27603-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-27603-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The import script cannot write to <code>settings/download.lock</code> for some reason. Most likely the user under which you are running the import script is not allowed to create a file in Nominatim/settings. This might happen, if you happen to run the script with <code>sudo -u postgres</code> or similar. The other possibility is that you have run the import script under a different user before, so that a stale <code>settings/download.lock</code> remained from this user and the current user is not allowed to change it. Simply delete the file in that case.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Oct '13, 21:55</strong></p>
<img src="https://secure.gravatar.com/avatar/d888b712d85dee0aa304297f2dc697c7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="lonvia&#39;s gravatar image" />
<p><span>lonvia</span><br />
<span class="score" title="6213 reputation points"><span>6.2k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="57 badges"><span class="silver">●</span><span class="badgecount">57</span></span><span title="89 badges"><span class="bronze">●</span><span class="badgecount">89</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="lonvia has 43 accepted answers">40%</span></p>
</div>
</div>
<div id="comments-container-27603" class="comments-container">
<span id="27631"></span>
<div id="comment-27631" class="comment">
<div id="post-27631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the suggestions. It doesn't look like a settings/download.lock file exists so I'm guessing my issue is the first one. Unfortunately, I'm a bit unclear as to how to fix it. The script I'm running is simply</p>
<p>./utils/setup.php --osm-file greenland.osm.pbf --all</p>
<p>Does the setup script call the import script? I've given my user sudoer privledges so I don't have to log in as root. Thanks for the help.</p>
</div>
<div id="comment-27631-info" class="comment-info">
<span class="comment-age">(29 Oct '13, 14:56)</span> <span class="comment-user userinfo">sbryfcz</span>
</div>
</div>
<span id="27790"></span>
<div id="comment-27790" class="comment">
<div id="post-27790-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I was able to clear up the lock error but still am getting the following errors related to opening stream. I spun up a test VM and was able to get everything working. So maybe its something I need my IT group to clear up on the server. Any suggestions?</p>
<p>... Nov 04, 2013 2:53:33 PM org.openstreetmap.osmosis.core.Osmosis run INFO: Total execution time: 322 milliseconds. PHP Warning: file_get_contents(<a href="http://www.openstreetmap.org/api/0.6/node/2506472169/1):">http://www.openstreetmap.org/api/0.6/node/2506472169/1):</a> failed to open stream: Connection timed out in /home/spbryfczynski/Documents/Nominatim/utils/setup.php on line 540 ...more errors</p>
</div>
<div id="comment-27790-info" class="comment-info">
<span class="comment-age">(04 Nov '13, 20:07)</span> <span class="comment-user userinfo">sbryfcz</span>
</div>
</div>
</div>
<div id="comment-tools-27603" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27603-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="27825"></span>

<div id="answer-container-27825" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-27825-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-27825-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-27825-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I ended up having to use curl for the file_get_contents methods (with urls). I added this function to the utils/setup.php file and then changed the file_get_contents calls to URLs to file_get_contents_curl. Things then worked.</p>
<pre><code>function file_get_contents_curl($url) {
      $ch = curl_init();
      curl_setopt($ch, CURLOPT_HEADER, 0);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); //Set curl to return the data instead of printing it to the $
      curl_setopt($ch, CURLOPT_URL, $url);
      $data = curl_exec($ch);
      curl_close($ch);
      return $data;
      }</code></pre>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 Nov '13, 14:21</strong></p>
<img src="https://secure.gravatar.com/avatar/cedcf7f648595f10a2eff219e1b94922?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="sbryfcz&#39;s gravatar image" />
<p><span>sbryfcz</span><br />
<span class="score" title="56 reputation points">56</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="sbryfcz has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-27825" class="comments-container">
&#10;</div>
<div id="comment-tools-27825" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-27825-form-container" class="comment-form-container">
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

