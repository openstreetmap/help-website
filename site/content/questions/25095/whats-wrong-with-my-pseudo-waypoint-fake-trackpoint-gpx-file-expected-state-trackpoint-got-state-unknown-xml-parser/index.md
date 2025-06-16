+++
type = "question"
title = "What&#x27;s wrong with my pseudo waypoint / fake trackpoint GPX file (&quot;Expected state TRACKPOINT, got state UNKNOWN XML parser&quot;)?"
description = '''I am lost with a GPX file. It was recorded with Quick Position App, then the names were stripped and the way points replaced with track points following the requirement of OSM. I was first getting (trying to upload to osm.org) the most informative Found no good GPX points in the input data (the reas...'''
date = "2013-08-08T23:06:00Z"
lastmod = "2013-08-11T15:11:00Z"
weight = 25095
keywords = [ "problem", "gpx", "upload" ]
aliases = [ "/questions/25095" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [What's wrong with my pseudo waypoint / fake trackpoint GPX file ("Expected state TRACKPOINT, got state UNKNOWN XML parser")?](/questions/25095/whats-wrong-with-my-pseudo-waypoint-fake-trackpoint-gpx-file-expected-state-trackpoint-got-state-unknown-xml-parser)

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
<span id="post-25095-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25095-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-25095-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am lost with a GPX file. It was recorded with Quick Position App, then the names were stripped and the way points replaced with track points following the <a href="https://wiki.openstreetmap.org/wiki/Gpx">requirement of OSM</a>. I was first getting (trying to upload to osm.org) the most informative <code>Found no good GPX points in the input data</code> (the reason being that the original file contained way points only), and now it's <code>Expected state TRACKPOINT, got state UNKNOWN XML parser at line 3 column 2</code>. I am stuck and would appreciate help.</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; standalone=&quot;no&quot; ?&gt;
&lt;gpx xmlns=&quot;http://www.topografix.com/GPX/1/1&quot; creator=&quot;matt&quot; version=&quot;1.1&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot; xsi:schemaLocation=&quot;http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd&quot;&gt;
        &lt;ele&gt;200.9063513539106&lt;/ele&gt;
        &lt;time&gt;1990-04-27T14-56-57Z&lt;/time&gt;
    &lt;/trkpt&gt;
    &lt;trkpt lat=&quot;54.55410358198684&quot; lon=&quot;25.3773501871292&quot;&gt;
    &lt;trkpt lat=&quot;54.55414923144265&quot; lon=&quot;25.377350253212516&quot;&gt;
        &lt;ele&gt;201.31068553007708&lt;/ele&gt;
        &lt;time&gt;1990-04-27T14-57-05Z&lt;/time&gt;
    &lt;/trkpt&gt;
    &lt;trkpt lat=&quot;54.55458511446888&quot; lon=&quot;25.37838106148478&quot;&gt;
        &lt;ele&gt;221.71354527843178&lt;/ele&gt;
        &lt;time&gt;1990-04-27T14-58-38Z&lt;/time&gt;
    &lt;/trkpt&gt;
    &lt;trkpt lat=&quot;54.554818184474456&quot; lon=&quot;25.378866436901745&quot;&gt;
        &lt;ele&gt;224.6318238358151&lt;/ele&gt;
        &lt;time&gt;1990-04-27T14-59-21Z&lt;/time&gt;
    &lt;/trkpt&gt;
    &lt;trkpt lat=&quot;54.554907515743935&quot; lon=&quot;25.379065394625034&quot;&gt;
        &lt;ele&gt;224.77350879803234&lt;/ele&gt;
        &lt;time&gt;1990-04-27T14-59-34Z&lt;/time&gt;
    &lt;/trkpt&gt;
&lt;/gpx&gt;</code></pre>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-problem" rel="tag" title="see questions tagged &#39;problem&#39;">problem</span> <span class="post-tag tag-link-gpx" rel="tag" title="see questions tagged &#39;gpx&#39;">gpx</span> <span class="post-tag tag-link-upload" rel="tag" title="see questions tagged &#39;upload&#39;">upload</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Aug '13, 23:06</strong></p>
<img src="https://secure.gravatar.com/avatar/7f75b476d4984deb5e4c83d276b9c22b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kotya&#39;s gravatar image" />
<p><span>Kotya</span><br />
<span class="score" title="631 reputation points">631</span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="36 badges"><span class="bronze">●</span><span class="badgecount">36</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kotya has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '13, 18:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-25095" class="comments-container">
&#10;</div>
<div id="comment-tools-25095" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25095-form-container" class="comment-form-container">
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

<span id="25096"></span>

<div id="answer-container-25096" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25096-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25096-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-25096-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Kotya has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The first trackpoint misses an begin tag and the second an end tag (that is no formally valid XML). I guess you swapped lines (line 6 should be line 3). The time format is wrong, too (apparently needs to be in <span>ISO 8601</span> format). Maybe <code>trk</code> and <code>trkseg</code> elements are needed too (it seems they are not for uploading to OSM, thanks <span><span>@Kotya</span></span> for testing it, maybe they are for standard compatibility). You can check your XML file by uploading or pasting at <a href="http://validator.w3.org/">http://validator.w3.org/</a> for <em>formal</em> errors. Suggestion:</p>
<pre><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot; standalone=&quot;no&quot; ?&gt;
&lt;gpx xmlns=&quot;http://www.topografix.com/GPX/1/1&quot; creator=&quot;matt&quot; version=&quot;1.1&quot; xmlns:xsi=&quot;http://www.w3.org/2001/XMLSchema-instance&quot; xsi:schemaLocation=&quot;http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd&quot;&gt;
&#10;&lt;trk&gt;
&lt;trkseg&gt;
    &lt;trkpt lat=&quot;54.55410358198684&quot; lon=&quot;25.3773501871292&quot;&gt;
        &lt;ele&gt;200.9063513539106&lt;/ele&gt;
        &lt;time&gt;1990-04-27T00:00:00Z&lt;/time&gt;
    &lt;/trkpt&gt;
        &lt;trkpt lat=&quot;54.55414923144265&quot; lon=&quot;25.377350253212516&quot;&gt;
        &lt;ele&gt;201.31068553007708&lt;/ele&gt;
        &lt;time&gt;1990-04-27T00:00:01Z&lt;/time&gt;
    &lt;/trkpt&gt;
    &lt;trkpt lat=&quot;54.55458511446888&quot; lon=&quot;25.37838106148478&quot;&gt;
        &lt;ele&gt;221.71354527843178&lt;/ele&gt;
        &lt;time&gt;1990-04-27T00:00:02Z&lt;/time&gt;
    &lt;/trkpt&gt;
    &lt;trkpt lat=&quot;54.554818184474456&quot; lon=&quot;25.378866436901745&quot;&gt;
        &lt;ele&gt;224.6318238358151&lt;/ele&gt;
        &lt;time&gt;1990-04-27T00:00:03Z&lt;/time&gt;
    &lt;/trkpt&gt;
    &lt;trkpt lat=&quot;54.554907515743935&quot; lon=&quot;25.379065394625034&quot;&gt;
        &lt;ele&gt;224.77350879803234&lt;/ele&gt;
        &lt;time&gt;1990-04-27T00:00:04Z&lt;/time&gt;
    &lt;/trkpt&gt;
&lt;/trkseg&gt;
&lt;/trk&gt;
&lt;/gpx&gt;</code></pre>
<p>Please delete such fake tracklogs (the connected waypoints make no sense I guess) after using it. By the way: with <span>Potlatch2</span> or JOSM you do not need to upload a gpx. You can even use a local gpx file with real waypoints. Despite that feature the obligatory warning: uploading tracks(!) is useful for other people (averaging several traces to try to eliminate some gps errors) - so, please continue to upload real tracks (maybe only if not tooo bad reception quality/smartphone/bad gps receiver).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Aug '13, 23:18</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Aug '13, 18:09</strong> </span></p>
</div>
</div>
<div id="comments-container-25096" class="comments-container">
<span id="25098"></span>
<div id="comment-25098" class="comment">
<div id="post-25098-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can I use a local file with Potlatch2? Could you explain how or give a link?</p>
</div>
<div id="comment-25098-info" class="comment-info">
<span class="comment-age">(08 Aug '13, 23:29)</span> <span class="comment-user userinfo">Kotya</span>
</div>
</div>
<span id="25099"></span>
<div id="comment-25099" class="comment">
<div id="post-25099-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for finding my stupid mistake. However, your code results in "Found no good GPX points in the input data. At least 75% of the trackpoints lacked a &lt;time&gt; tag." :) Any clue?</p>
</div>
<div id="comment-25099-info" class="comment-info">
<span class="comment-age">(08 Aug '13, 23:31)</span> <span class="comment-user userinfo">Kotya</span>
</div>
</div>
<span id="25101"></span>
<div id="comment-25101" class="comment">
<div id="post-25101-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Inserted link for Potlatch2. Fixed the time - did you break the precious gpx file in even more ways? ;-)</p>
</div>
<div id="comment-25101-info" class="comment-info">
<span class="comment-age">(08 Aug '13, 23:39)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="25109"></span>
<div id="comment-25109" class="comment not_top_scorer">
<div id="post-25109-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, it was not me! :) OSM does not like way points, and the app does not know the standards :) BTW, thanks for correcting my XML code formatting. I know the rules, but the preview here fails on the properly formatted code. So I "corrected" it to make sure you can at least see what I mean. Thanks for undoing it.</p>
</div>
<div id="comment-25109-info" class="comment-info">
<span class="comment-age">(09 Aug '13, 07:20)</span> <span class="comment-user userinfo">Kotya</span>
</div>
</div>
<span id="25110"></span>
<div id="comment-25110" class="comment">
<div id="post-25110-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>BTW, the <code>trk</code> and <code>trkseg</code> elements are not needed. Apparently, I cannot edit your answer.</p>
</div>
<div id="comment-25110-info" class="comment-info">
<span class="comment-age">(09 Aug '13, 07:27)</span> <span class="comment-user userinfo">Kotya</span>
</div>
</div>
<span id="25127"></span>
<div id="comment-25127" class="comment">
<div id="post-25127-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for the report, I have added it (see <a href="https://help.openstreetmap.org/faq/">faq about karma</a> why you cannot edit my answer).</p>
<p>I hope you got the direct loading in Potlatch2 to work, too.</p>
</div>
<div id="comment-25127-info" class="comment-info">
<span class="comment-age">(09 Aug '13, 18:10)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-25096" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-25096-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="25203"></span>

<div id="answer-container-25203" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-25203-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-25203-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-25203-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You don't need to convert waypoints to trackpoints - leave the waypoints as is and add a fake track segment and track point corresponding to the first waypoint.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 Aug '13, 15:07</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-25203" class="comments-container">
<span id="25204"></span>
<div id="comment-25204" class="comment">
<div id="post-25204-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Ah, yeah, indeed. I missed to mention that. However, if you only want to use the waypoints yourself (not <a href="/questions/24804/where-can-i-upload-my-surveys-with-pois">for use by other mappers</a>), then uploading waypoints is not needed at all - and therefore even more easy (no editing needed).</p>
</div>
<div id="comment-25204-info" class="comment-info">
<span class="comment-age">(11 Aug '13, 15:11)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-25203" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-25203-form-container" class="comment-form-container">
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

