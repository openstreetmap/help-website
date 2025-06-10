+++
type = "question"
title = "Osmosis Cannot begin reading in Add stage, must call complete first. ERROR"
description = '''I am trying to compile a map, I added fake version and fake author with osmconvert. But I am getting this error. Btw I am using latest stable. The command I have used:  bin/osmosis --rx file=&quot;engineering-raw-auth-version.osm&quot; --mapfile-writer file=engineering-base-drawing.map type=hd tag-conf-file=t...'''
date = "2022-08-18T13:35:00Z"
lastmod = "2022-08-18T14:00:00Z"
weight = 85374
keywords = [ "osmosis" ]
aliases = [ "/questions/85374" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Osmosis Cannot begin reading in Add stage, must call complete first. ERROR](/questions/85374/osmosis-cannot-begin-reading-in-add-stage-must-call-complete-first-error)

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
<span id="post-85374-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85374-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85374-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to compile a map, I added fake version and fake author with osmconvert. But I am getting this error. Btw I am using latest stable. The command I have used:</p>
<p>bin/osmosis --rx file="engineering-raw-auth-version.osm" --mapfile-writer file=engineering-base-drawing.map type=hd tag-conf-file=tag-mapping.xml tag-values=true</p>
<p>```` org.openstreetmap.osmosis.core.OsmosisRuntimeException: Cannot begin reading in Add stage, must call complete first. at org.openstreetmap.osmosis.core.store.RandomAccessObjectStore.initializeReadingStage(RandomAccessObjectStore.java:156) at org.openstreetmap.osmosis.core.store.RandomAccessObjectStore.createReader(RandomAccessObjectStore.java:181) at org.openstreetmap.osmosis.core.store.IndexStore.createReader(IndexStore.java:151) at org.openstreetmap.osmosis.core.store.IndexedObjectStore.createReader(IndexedObjectStore.java:96) at org.mapsforge.map.writer.HDTileBasedDataProcessor.complete(HDTileBasedDataProcessor.java:132) at org.mapsforge.map.writer.osmosis.MapFileWriterTask.complete(MapFileWriterTask.java:104) at org.openstreetmap.osmosis.xml.v0_6.XmlReader.run(XmlReader.java:53) at java.base/java.lang.Thread.run(Thread.java:834)</p>
<p>Aug 18, 2022 3:30:15 PM org.openstreetmap.osmosis.core.Osmosis main SEVERE: Execution aborted. org.openstreetmap.osmosis.core.OsmosisRuntimeException: One or more tasks failed. at org.openstreetmap.osmosis.core.pipeline.common.Pipeline.waitForCompletion(Pipeline.java:146) at org.openstreetmap.osmosis.core.Osmosis.run(Osmosis.java:92) at org.openstreetmap.osmosis.core.Osmosis.main(Osmosis.java:37) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method) at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62) at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43) at java.base/java.lang.reflect.Method.invoke(Method.java:566) at org.codehaus.plexus.classworlds.launcher.Launcher.launchStandard(Launcher.java:330) at org.codehaus.plexus.classworlds.launcher.Launcher.launch(Launcher.java:238) at org.codehaus.plexus.classworlds.launcher.Launcher.mainWithExitCode(Launcher.java:415) at org.codehaus.plexus.classworlds.launcher.Launcher.main(Launcher.java:356) at org.codehaus.classworlds.Launcher.main(Launcher.java:47) ````</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osmosis" rel="tag" title="see questions tagged &#39;osmosis&#39;">osmosis</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Aug '22, 13:35</strong></p>
<img src="https://secure.gravatar.com/avatar/7f1c260e99dffff55f895757e570cf43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baranacikgoz&#39;s gravatar image" />
<p><span>baranacikgoz</span><br />
<span class="score" title="76 reputation points">76</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baranacikgoz has 2 accepted answers">100%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Aug '22, 13:58</strong> </span></p>
</div>
</div>
<div id="comments-container-85374" class="comments-container">
<span id="85375"></span>
<div id="comment-85375" class="comment">
<div id="post-85375-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Two questions:</p>
<p>1) What osmosis command did you actually run?</p>
<p>2) What is your end goal? I'm not sure what "compile a map" means, and it may be there is a better way to do whatever it is that you are trying to do.</p>
</div>
<div id="comment-85375-info" class="comment-info">
<span class="comment-age">(18 Aug '22, 13:46)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="85376"></span>
<div id="comment-85376" class="comment">
<div id="post-85376-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, the command was I use:</p>
<p>bin/osmosis --rx file="engineering-raw-auth-version.osm" --mapfile-writer file=engineering-base-drawing.map type=hd tag-conf-file=tag-mapping.xml tag-values=true</p>
</div>
<div id="comment-85376-info" class="comment-info">
<span class="comment-age">(18 Aug '22, 13:58)</span> <span class="comment-user userinfo">baranacikgoz</span>
</div>
</div>
</div>
<div id="comment-tools-85374" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85374-form-container" class="comment-form-container">
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

<span id="85377"></span>

<div id="answer-container-85377" class="answer accepted-answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-85377-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-85377-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-85377-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="SomeoneElse has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I just removed the type=hd and it worked.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '22, 14:00</strong></p>
<img src="https://secure.gravatar.com/avatar/7f1c260e99dffff55f895757e570cf43?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="baranacikgoz&#39;s gravatar image" />
<p><span>baranacikgoz</span><br />
<span class="score" title="76 reputation points">76</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="7 badges"><span class="bronze">●</span><span class="badgecount">7</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="baranacikgoz has 2 accepted answers">100%</span></p>
</div>
</div>
<div id="comments-container-85377" class="comments-container">
&#10;</div>
<div id="comment-tools-85377" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-85377-form-container" class="comment-form-container">
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

