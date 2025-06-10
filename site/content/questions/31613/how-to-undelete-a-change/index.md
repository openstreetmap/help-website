+++
type = "question"
title = "How to undelete a change"
description = '''I accidentally deleted two towers (I don&#x27;t remember deleting them, but they&#x27;re in my history). I was trying to restore them, but I can&#x27;t figure out how.   Version #2 · Changeset #21148185 Location: 29.4663649, -95.2234284'''
date = "2014-03-17T02:52:00Z"
lastmod = "2014-03-17T08:06:00Z"
weight = 31613
keywords = [ "undelete" ]
aliases = [ "/questions/31613" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [How to undelete a change](/questions/31613/how-to-undelete-a-change)

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
<span id="post-31613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31613-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-31613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I accidentally deleted two towers (I don't remember deleting them, but they're in my history). I was trying to restore them, but I can't figure out how.<br />
</p>
<p>Version #2 · Changeset #21148185 Location: 29.4663649, -95.2234284</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-undelete" rel="tag" title="see questions tagged &#39;undelete&#39;">undelete</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Mar '14, 02:52</strong></p>
<img src="https://secure.gravatar.com/avatar/922ff83a83d541d1a8fd4ceab548b23d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rmavery&#39;s gravatar image" />
<p><span>rmavery</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rmavery has no accepted answers">0%</span> </br></p>
</div>
</div>
<div id="comments-container-31613" class="comments-container">
<span id="31621"></span>
<div id="comment-31621" class="comment">
<div id="post-31621-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I've undeleted it (see answer below) but have subsequently completely re-worked the nodes because they were very out-of-date inaccurate data from a 1994 (!!) GNIS dataset. The two towers were also but one, so one of them got re-deleted.</p>
</div>
<div id="comment-31621-info" class="comment-info">
<span class="comment-age">(17 Mar '14, 08:06)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-31613" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31613-form-container" class="comment-form-container">
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

<span id="31619"></span>

<div id="answer-container-31619" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-31619-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-31619-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-31619-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As a long time user of OpenStreetMap I keep a way of accessing an old editor (Potlatch 1) open as that had an undelete function. However, I would not recommend that approach in general.</p>
<p>The <strong>best way</strong> to approach this is to use JOSM.</p>
<p>There are a fairly sensible set of steps, but they are not particularly clear, partly because the interface for accessing them has changed from time to time. You may need one or more of the following plugins : reverter, changeset manager and undelete. (Unfortunately, as I have them all installed I'm exactly sure which one does what). If you are not familiar with JOSM it is best to ask someone else to do it for you: the learning curve required on your behalf may be totally disproportionate to the effort required by an experienced user.</p>
<p>As you already know identifying the changeset (for complete reversion) and individual object ids (for minor undeletes) is the most useful information to start with. In your case the deleted object is a nodes: <a href="http://www.openstreetmap.org/node/356756834">356756834</a>. The other tower looks fine, although it is attached to a road: <a href="http://www.openstreetmap.org/node/356756961/history">356756961</a>. So this is a simple case and the undelete option (on JOSM File menu) can be used.</p>
<ol>
<li>Select File|Undelete object ...</li>
<li>Enter "n" followed by the node id (aside to JOSM developers: this dialog should be re-designed to provide a selection list for object type as the requirement for an object type prefix is <strong>non-intuitive</strong>), i.e., "n356756834"</li>
<li>Select the "Separate Layer" option. (This helps if anything goes wrong).</li>
<li>Click OK.</li>
<li>Check that the object is as you expected.</li>
<li>Upload back to OSM.</li>
</ol>
<p>You can do the same thing with Changeset Manager (overkill for this example) which hides away under the Windows menu.</p>
<p>I've gone and undeleted the object, detached the other tower from the road and tweaked their positions a bit (these came from GNIS so positional accuracy is not always fantastic).</p>
<p>In fact the names of these transmitters seem completely at variance with information on wikipedia (KRTS is given <a href="http://en.wikipedia.org/wiki/KRTS">there</a> as being in a mountainous region of West Texas) and there is only one tower visible on Bing imagery). An inspection of the wikipedia article on <a href="http://en.wikipedia.org/wiki/KROI">KROI</a> suggests part of the problem: the GNIS import is so out-of-date as to be worthless. So I shouldn't have really undeleted this node as you actually inadvertently improved the map!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Mar '14, 07:18</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>24 Jul '15, 11:14</strong> </span></p>
</div>
</div>
<div id="comments-container-31619" class="comments-container">
&#10;</div>
<div id="comment-tools-31619" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-31619-form-container" class="comment-form-container">
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

