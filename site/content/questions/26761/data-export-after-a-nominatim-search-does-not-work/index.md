+++
type = "question"
title = "Data export after a nominatim search does not work"
description = '''When I type a location into OSM it gives me a choice of loading the map from nominatim or some other device but I loose the export facility. How can I overcome this?'''
date = "2013-09-26T09:09:00Z"
lastmod = "2013-09-26T13:31:00Z"
weight = 26761
keywords = [ "osm.org", "nominatim", "export" ]
aliases = [ "/questions/26761" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Data export after a nominatim search does not work](/questions/26761/data-export-after-a-nominatim-search-does-not-work)

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
<span id="post-26761-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26761-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-26761-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When I type a location into OSM it gives me a choice of loading the map from nominatim or some other device but I loose the export facility. How can I overcome this?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osm.org" rel="tag" title="see questions tagged &#39;osm.org&#39;">osm.org</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-export" rel="tag" title="see questions tagged &#39;export&#39;">export</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>26 Sep '13, 09:09</strong></p>
<img src="https://secure.gravatar.com/avatar/ffc431f8d31c092e92a085f053087642?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="riwood&#39;s gravatar image" />
<p><span>riwood</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="riwood has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>19 Oct '13, 22:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-26761" class="comments-container">
&#10;</div>
<div id="comment-tools-26761" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26761-form-container" class="comment-form-container">
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

<span id="26780"></span>

<div id="answer-container-26780" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-26780-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-26780-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-26780-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>assuming you mean the data export on osm.org:</p>
<p>I, using Firefox, can confirm that (it is like that since the homepage redesign). The data export (via link on the left panel) does not use the screen view which was currently displayed (e.g. after a nominatim search).</p>
<p>I found a <em>own cookie for /export/</em> which seems to have been the problem. I deleted it manually - now it works as expected (and no new /export/ cookie gets set). Maybe try to delete that cookie, too (if you have it). On openstreetmap.org: Ctrl+I, security tab, show cookies, and then ...</p>
<p><span><img src="/upfiles/exportcookiemark2.png" width="509" height="115" alt="firefox cookie list dialog screenshot with arrows" /></span></p>
<p>Please comment if you meant that and if it works for you.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Sep '13, 13:31</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Sep '13, 13:33</strong> </span></p>
</div>
</div>
<div id="comments-container-26780" class="comments-container">
&#10;</div>
<div id="comment-tools-26780" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-26780-form-container" class="comment-form-container">
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

