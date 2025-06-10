+++
type = "question"
title = "Why do most bridges under man_made show up in turbo &quot;bridges&quot; search"
description = '''On https://overpass-turbo.eu/ I am using the tag request clause &quot;bridge&quot; not just bridge, so shouldn&#x27;t it limit it to bridges that have that key, yet many or most of results show man_made=bridges in listed tags when I open up from results map, but not key Bridges tag. Example is the famous Brooklyn ...'''
date = "2019-05-28T11:44:00Z"
lastmod = "2019-05-28T13:36:00Z"
weight = 69344
keywords = [ "overpass-turbo", "key" ]
aliases = [ "/questions/69344" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Why do most bridges under man_made show up in turbo "bridges" search](/questions/69344/why-do-most-bridges-under-man_made-show-up-in-turbo-bridges-search)

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
<span id="post-69344-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69344-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-69344-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>On <a href="https://overpass-turbo.eu/">https://overpass-turbo.eu/</a> I am using the tag request clause "bridge" not just bridge, so shouldn't it limit it to bridges that have that key, yet many or most of results show man_made=bridges in listed tags when I open up from results map, but not key Bridges tag. Example is the famous Brooklyn Bridge. There are only approx. 60,000 man_made=bridge in OSM yet it seems they all show up under bridge key search, yet bridge has millions in OSM. Can someone explain? <a href="https://www.openstreetmap.org/way/375157262">https://www.openstreetmap.org/way/375157262</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass-turbo" rel="tag" title="see questions tagged &#39;overpass-turbo&#39;">overpass-turbo</span> <span class="post-tag tag-link-key" rel="tag" title="see questions tagged &#39;key&#39;">key</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 May '19, 11:44</strong></p>
<img src="https://secure.gravatar.com/avatar/aa3e93cbd0a635b436a0ca3a776156ca?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="philip&#39;s gravatar image" />
<p><span>philip</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="philip has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 May '19, 11:47</strong> </span></p>
</div>
</div>
<div id="comments-container-69344" class="comments-container">
&#10;</div>
<div id="comment-tools-69344" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69344-form-container" class="comment-form-container">
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

<span id="69345"></span>

<div id="answer-container-69345" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-69345-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-69345-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-69345-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It looks like overpass turbo's wizard translates <code>"bridge"</code> to <code>man_made=bridge</code> as shown here:</p>
<pre><code>/*
This has been generated by the overpass-turbo wizard.
The original search was:
“&quot;bridge&quot;”
*/
[out:json][timeout:25];
// gather results
(
  // query part for: “bridge”
  way[&quot;man_made&quot;=&quot;bridge&quot;]({{bbox}});
  relation[&quot;man_made&quot;=&quot;bridge&quot;]({{bbox}});
);
// print results
out body;
&gt;;
out skel qt;</code></pre>
<p>You probably want to try <code>"bridge"=*</code></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 May '19, 11:54</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-69345" class="comments-container">
<span id="69347"></span>
<div id="comment-69347" class="comment">
<div id="post-69347-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, that did it! Thank you. I thought that I was looking at all key=bridges but I was actually looking at man_made=bridges. But that is really strange they do that automatic modification of search when person uses the correct clause, no? The one you provided doesn't even seem to be in tag request clause section here. Or maybe I need to read it more thoroughly. <a href="https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide">https://wiki.openstreetmap.org/wiki/Overpass_API/Language_Guide</a> Thx again.</p>
<p>EDIT but I just noticed something else...when I search by Man-made=bridge the tag "Bridge=yes" does not show up on Brooklyn bridge info on left, yet when I search your new search it's visa versa...man_made=bridge does not show up on left, only bridge=yes. I had assumed it showed all tags over there? Seems to only show tag you were looking for and a few others.</p>
</div>
<div id="comment-69347-info" class="comment-info">
<span class="comment-age">(28 May '19, 12:03)</span> <span class="comment-user userinfo">philip</span>
</div>
</div>
<span id="69350"></span>
<div id="comment-69350" class="comment">
<div id="post-69350-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The left panel only displays the query. It contains only the tags you are searching for. Or better the tags which the overpass turbo wizard <em>thinks</em> you are searching for. To see all tags of the found objects you have to look at the results, not at the query.</p>
</div>
<div id="comment-69350-info" class="comment-info">
<span class="comment-age">(28 May '19, 13:36)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-69345" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-69345-form-container" class="comment-form-container">
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

