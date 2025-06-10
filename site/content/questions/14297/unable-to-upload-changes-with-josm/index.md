+++
type = "question"
title = "unable to upload changes with JOSM"
description = '''Hello, I&#x27;ve added some building in my city in JOSM, and when I try to upload the changes, I get the following error message in the console :  PUT http://api.openstreetmap.org/api/0.6/changeset/create... Forbidden Error header: Your access to the API has been blocked. Please log-in to the web interfa...'''
date = "2012-07-16T13:07:00Z"
lastmod = "2012-07-17T11:09:00Z"
weight = 14297
keywords = [ "josm", "http_403_forbidden", "changes", "upload" ]
aliases = [ "/questions/14297" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [unable to upload changes with JOSM](/questions/14297/unable-to-upload-changes-with-josm)

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
<span id="post-14297-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14297-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-14297-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I've added some building in my city in JOSM, and when I try to upload the changes, I get the following error message in the console :</p>
<blockquote>
<p>PUT <a href="http://api.openstreetmap.org/api/0.6/changeset/create...">http://api.openstreetmap.org/api/0.6/changeset/create...</a> Forbidden Error header: <strong>Your access to the API has been blocked. Please log-in to the web interface to find out more.</strong> org.openstreetmap.josm.io.OsmApiException: ResponseCode=403, Error Header=&lt;your access="" to="" the="" api="" has="" been="" blocked.="" please="" log-in="" to="" the="" web="" interface="" to="" find="" out="" more.=""&gt; at org.openstreetmap.josm.io.OsmApi.sendRequest(OsmApi.java:657) at org.openstreetmap.josm.io.OsmApi.sendRequest(OsmApi.java:534) at org.openstreetmap.josm.io.OsmApi.openChangeset(OsmApi.java:372) at org.openstreetmap.josm.io.OsmServerWriter.uploadOsm(OsmServerWriter.java:201) at org.openstreetmap.josm.gui.io.UploadPrimitivesTask.realRun(UploadPrimitivesTask.java:246) at org.openstreetmap.josm.gui.PleaseWaitRunnable.doRealRun(PleaseWaitRunnable.java:82) at org.openstreetmap.josm.gui.PleaseWaitRunnable.run(PleaseWaitRunnable.java:145) at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1110) at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:603) at java.lang.Thread.run(Thread.java:722)</p>
</blockquote>
<p>I already made some modifications yesterday with JOSM, and it worked fine. I'm using the tested version of JOSM (v 5315)</p>
<p>Edit : According to <a href="http://osdir.com/ml/gis.openstreetmap.user/2007-10/msg00030.html">http://osdir.com/ml/gis.openstreetmap.user/2007-10/msg00030.html</a> it seemed that using josm-latest would have solved the problem, bu I still can't upload my changes ...</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-josm" rel="tag" title="see questions tagged &#39;josm&#39;">josm</span> <span class="post-tag tag-link-http_403_forbidden" rel="tag" title="see questions tagged &#39;http_403_forbidden&#39;">http_403_forbidden</span> <span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Jul '12, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/4e24701fe902967ca63e4105daf37431?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="znarf94&#39;s gravatar image" />
<p><span>znarf94</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="znarf94 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Dec '18, 22:37</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-14297" class="comments-container">
<span id="14301"></span>
<div id="comment-14301" class="comment">
<div id="post-14301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>No - see Gnonthgol's answer below.</p>
</div>
<div id="comment-14301-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 13:26)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="14303"></span>
<div id="comment-14303" class="comment">
<div id="post-14303-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Here is the reason of the blocking : "The OSM Sysadmins have requested that all imports, automated edits, bulk edits and bots be stopped until the redaction process has ended." But what is that "redaction process" ? Sorry, I'm new to OSM</p>
</div>
<div id="comment-14303-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 13:34)</span> <span class="comment-user userinfo">znarf94</span>
</div>
</div>
<span id="14306"></span>
<div id="comment-14306" class="comment">
<div id="post-14306-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>If you're new to OSM you should <em>not</em> be importing data. See <a href="http://wiki.openstreetmap.org/wiki/Imports">http://wiki.openstreetmap.org/wiki/Imports</a> : "Scripted imports and automated edits should only be carried out by those with experience and understanding of the way the OpenStreetMap community creates maps".</p>
</div>
<div id="comment-14306-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 13:42)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="14308"></span>
<div id="comment-14308" class="comment">
<div id="post-14308-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Sorry, but it's the the only way I found to create missing bulidings and tracks precisely</p>
</div>
<div id="comment-14308-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 14:01)</span> <span class="comment-user userinfo">znarf94</span>
</div>
</div>
<span id="14315"></span>
<div id="comment-14315" class="comment">
<div id="post-14315-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>(Ignoring all the other potential issues) unless you've been there, how do you know that a particular track still exists? How do you know that the way that it's described on the other map is how it should be tagged in OSM?</p>
</div>
<div id="comment-14315-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 15:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-14297" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-14297-form-container" class="comment-form-container">
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

<span id="14298"></span>

<div id="answer-container-14298" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-14298-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-14298-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-14298-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="znarf94 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>That means that someone have blocked you from uploading any changes to osm. If you log in to the <a href="https://www.openstreetmap.org/login">web interface</a> you find out who and why you are blocked.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jul '12, 13:17</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jul '12, 13:18</strong> </span></p>
</div>
</div>
<div id="comments-container-14298" class="comments-container">
<span id="14300"></span>
<div id="comment-14300" class="comment">
<div id="post-14300-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ok, I went on the web interface and now it works ! Is there any problem when importing data from the french cadastre ?</p>
</div>
<div id="comment-14300-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 13:24)</span> <span class="comment-user userinfo">znarf94</span>
</div>
</div>
<span id="14304"></span>
<div id="comment-14304" class="comment">
<div id="post-14304-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>At the moment all imports should be suspended because of the redaction bot. It is causing the redaction bot to fail areas when someone edits it at the same time, and it is slowing down the database and causing the redaction bot to fail.</p>
</div>
<div id="comment-14304-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 13:37)</span> <span class="comment-user userinfo">Gnonthgol ♦</span>
</div>
</div>
<span id="14305"></span>
<div id="comment-14305" class="comment">
<div id="post-14305-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ok, and when will this bot have finished ?</p>
</div>
<div id="comment-14305-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 13:39)</span> <span class="comment-user userinfo">znarf94</span>
</div>
</div>
<span id="14318"></span>
<div id="comment-14318" class="comment">
<div id="post-14318-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A month's time or more.</p>
</div>
<div id="comment-14318-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 16:15)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
<span id="14326"></span>
<div id="comment-14326" class="comment">
<div id="post-14326-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>And you will be blocked again, and your edits reverted, if you are found to be doing an import that has not been discussed on the "imports" mailing list before. So why not use the time between now and then to hone your communications skills.</p>
</div>
<div id="comment-14326-info" class="comment-info">
<span class="comment-age">(16 Jul '12, 19:58)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="14336"></span>
<div id="comment-14336" class="comment not_top_scorer">
<div id="post-14336-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok, I wait. Sorry, my english is not perfect, I try to improve myself</p>
</div>
<div id="comment-14336-info" class="comment-info">
<span class="comment-age">(17 Jul '12, 11:09)</span> <span class="comment-user userinfo">znarf94</span>
</div>
</div>
</div>
<div id="comment-tools-14298" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-14298-form-container" class="comment-form-container">
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

