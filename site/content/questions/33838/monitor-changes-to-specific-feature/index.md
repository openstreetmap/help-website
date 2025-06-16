+++
type = "question"
title = "Monitor changes to specific feature"
description = '''I am aware of WHODIDIT, which lets you monitor changes in a given area, but I would like to monitor changes to a list of specific relations and ways (a few hundreds of them) which are not necessarily close to one another. For example, I would like to know when the boundary of a certain city is modif...'''
date = "2014-06-10T02:32:00Z"
lastmod = "2014-06-14T11:33:00Z"
weight = 33838
keywords = [ "changes", "history" ]
aliases = [ "/questions/33838" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Monitor changes to specific feature](/questions/33838/monitor-changes-to-specific-feature)

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
<span id="post-33838-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33838-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-33838-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am aware of WHODIDIT, which lets you monitor changes in a given area, but I would like to monitor changes to a list of specific relations and ways (a few hundreds of them) which are not necessarily close to one another. For example, I would like to know when the boundary of a certain city is modified.</p>
<p>Is there any tool that allows you to do that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span> <span class="post-tag tag-link-history" rel="tag" title="see questions tagged &#39;history&#39;">history</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Jun '14, 02:32</strong></p>
<img src="https://secure.gravatar.com/avatar/245cb5e781c1e0ce4e41027252ef9377?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Augusto%20S&#39;s gravatar image" />
<p><span>Augusto S</span><br />
<span class="score" title="111 reputation points">111</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="8 badges"><span class="bronze">●</span><span class="badgecount">8</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Augusto S has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-33838" class="comments-container">
<span id="33974"></span>
<div id="comment-33974" class="comment">
<div id="post-33974-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Be aware that this involves more than just the relation and ways. A boundary also changes whenever one of the way's nodes get moved. But changes in the position or the tags of a node are not recorded in the way's history. So you way want to monitor each single node, too.</p>
</div>
<div id="comment-33974-info" class="comment-info">
<span class="comment-age">(14 Jun '14, 10:52)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="33975"></span>
<div id="comment-33975" class="comment">
<div id="post-33975-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>This is exactly covered by the Overpass API example I provided below. You just have to define which objects (and depending objects) you want to include in your change analysis.</p>
</div>
<div id="comment-33975-info" class="comment-info">
<span class="comment-age">(14 Jun '14, 11:33)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-33838" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33838-form-container" class="comment-form-container">
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

<span id="33965"></span>

<div id="answer-container-33965" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33965-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33965-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-33965-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Overpass API can indeed help, at least starting with v0.7.50. As an example, you could query for changes to ways 5000000 + 5000001 (including their nodes) since January 1st 2012:</p>
<pre><code>[adiff:&quot;2012-01-01T00:00:00Z&quot;];(way(5000000);&gt;;way(5000001);&gt;;);out meta;</code></pre>
<p><a href="http://overpass-turbo.eu/s/3JL">Try this on turbo</a> and <strong>switch to the Data tab</strong> to see old/new data as well as the type of change (create/modify/delete).</p>
<p>Note that there are no changes shown for way 5000001 as there weren't any in the last 5 years. Also some of the changes may no longer be available due to the License redaction bot. As a general rule of thumb, all changes since September 2012 should not be impacted by the bot.</p>
<p>For advanced visualization of augmented diffs please refer to <a href="https://github.com/tyrasd/overpass-ide/issues/80">Overpass Turbo Issue #80</a> (in planning phase at the time of writing this comment).</p>
</div>
<div class="answer-controls post-controls">
<div class="community-wiki">
This answer is marked "community wiki".
</div>
</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '14, 19:53</strong></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mmd has 44 accepted answers">37%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Jun '14, 19:57</strong> </span></p>
</div>
</div>
<div id="comments-container-33965" class="comments-container">
&#10;</div>
<div id="comment-tools-33965" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33965-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="33962"></span>

<div id="answer-container-33962" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-33962-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-33962-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-33962-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Maybe you are able to load each relation element from the main OSM database with full meta data.</p>
<p>This should include the version number of each object, and if I am not wrong even a timestamp when it was modified the last time.</p>
<p>Each time when an OSM object is edited, the version number is increased by 1.</p>
<p>Try to store the version number of each object in a file or database of your choice. Then compare that stored version number with the result when you want to check it.</p>
<p>Perhabs you can benefit from the famous <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">overpass-api</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Jun '14, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-33962" class="comments-container">
&#10;</div>
<div id="comment-tools-33962" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-33962-form-container" class="comment-form-container">
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

