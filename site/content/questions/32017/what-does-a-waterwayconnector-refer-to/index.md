+++
type = "question"
title = "What does a waterway=connector refer to?"
description = '''I&#x27;m starting to investigate the possibility of advocating for some sort of highway=waterway tag to describe the portions of a canoe or boat route that pass over lakes or ponds.  I came across the tag waterway=connector on Taginfo today. There are 482 occurrences of this tag in existence. I&#x27;ve run a ...'''
date = "2014-03-31T12:22:00Z"
lastmod = "2014-04-01T10:54:00Z"
weight = 32017
keywords = [ "connector", "waterway", "tags" ]
aliases = [ "/questions/32017" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What does a waterway=connector refer to?](/questions/32017/what-does-a-waterwayconnector-refer-to)

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
<span id="post-32017-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32017-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32017-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm starting to investigate the possibility of advocating for some sort of highway=waterway tag to describe the portions of a canoe or boat route that pass over lakes or ponds.</p>
<p>I came across the tag waterway=connector on Taginfo today. There are 482 occurrences of this tag in existence. I've run a bunch of queries with Overpass but cannot seem to locate one of these to inspect.</p>
<p>I was thinking it might be useful to describe the lake crossing portions of a canoe route, thus acting as a "connector" to the footway portions (the portages).</p>
<p>Anyone know what it's for or how it's used?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-connector" rel="tag" title="see questions tagged &#39;connector&#39;">connector</span> <span class="post-tag tag-link-waterway" rel="tag" title="see questions tagged &#39;waterway&#39;">waterway</span> <span class="post-tag tag-link-tags" rel="tag" title="see questions tagged &#39;tags&#39;">tags</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Mar '14, 12:22</strong></p>
<img src="https://secure.gravatar.com/avatar/04dddf6f5ffde333747d385af3ce5829?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AlaskaDave&#39;s gravatar image" />
<p><span>AlaskaDave</span><br />
<span class="score" title="5415 reputation points"><span>5.4k</span></span><span title="76 badges"><span class="badge1">●</span><span class="badgecount">76</span></span><span title="107 badges"><span class="silver">●</span><span class="badgecount">107</span></span><span title="164 badges"><span class="bronze">●</span><span class="badgecount">164</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AlaskaDave has 17 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-32017" class="comments-container">
&#10;</div>
<div id="comment-tools-32017" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32017-form-container" class="comment-form-container">
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

<span id="32021"></span>

<div id="answer-container-32021" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32021-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Waterway connector is probably a 1:1 mapping from <a href="http://wiki.openstreetmap.org/wiki/NHD">US NHD</a> data.</p>
<p>IIRC this is used to indicate the flowline of a linear waterway (river, stream etc) through a lake, pond or reservoir. There are advantages to this approach: if connector is not rendered then one gets a better rendering; the entire flow of a catchment is still captured (which it would not be if there is no linear waterway through water bodies). The downside is that it might not capture all the information one might want (e.g., does it represent a river or stream).</p>
<p>Another name in NHD s ArtificalPath.</p>
<p>I'm not aware that we had any detailed discussion about the use of such features in OSM, although my belief is that used judiciously they can make working with river catchment data from OSM much easier.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Mar '14, 14:01</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-32021" class="comments-container">
<span id="32023"></span>
<div id="comment-32023" class="comment">
<div id="post-32023-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It's really, really important to document such tags in the wiki. I can easily forgive if someone deletes/cleans-up undocumented/encrypted tags. OSM is not just a collection of private contributions. We need to understand what others are doing. And if the tag is not self-explanatory, the explanations have to be in the OSM wiki.</p>
</div>
<div id="comment-32023-info" class="comment-info">
<span class="comment-age">(31 Mar '14, 15:16)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
<span id="32027"></span>
<div id="comment-32027" class="comment">
<div id="post-32027-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I agree with that Pieren.</p>
<p>So it's likely a left-over from a big NHD import then. Strangely enough, I didn't search for it the the U.S. but in Europe, figuring the European OSM community is way ahead of those of us mapping in the United States.</p>
<p>I added a canoe route to OSM a few weeks ago and I was tempted to draw artificial steams across the lakes just so they would show up as ways to be followed — useful information to have in situations where the trail divides into a longer and a shorter route, as does the trail I added. I wonder if these connectors appear as ways?</p>
<p>Thanks much.</p>
</div>
<div id="comment-32027-info" class="comment-info">
<span class="comment-age">(31 Mar '14, 17:28)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="32028"></span>
<div id="comment-32028" class="comment">
<div id="post-32028-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@Pieren</span> just because I provided an explanation does not mean that I have ever used the tag, nor did I know it had been used on OSM until today. You imply that this is my responsibility. It is not. I would appreciate clarification of your comment in this light.</p>
<p><span>@AlaskaDave</span>: I am speculating that its an NHD feature because I have seen it there (as documented on the Wiki :-) ). If it appears in Europe then there may be another explanation, although I'm sure it is similar.</p>
</div>
<div id="comment-32028-info" class="comment-info">
<span class="comment-age">(31 Mar '14, 18:04)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="32036"></span>
<div id="comment-32036" class="comment">
<div id="post-32036-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I finally found some. They are all located in a section of the Colorado dry plains and are probably similar to intermittent streams except perhaps even more intermittent. They are not rendered, no surprise there, and were added by user:nhd_import back in 2009.</p>
<p>Not of any further interest to me, and probably nobody else either if I was to venture a guess.</p>
</div>
<div id="comment-32036-info" class="comment-info">
<span class="comment-age">(01 Apr '14, 05:41)</span> <span class="comment-user userinfo">AlaskaDave</span>
</div>
</div>
<span id="32041"></span>
<div id="comment-32041" class="comment">
<div id="post-32041-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@SK53</span> I'm not pointing out one particular person. The question is about a tag that I wasn't aware and unable to find in the wiki. You are the one who submitted a (possible) explanation. Fine. If this is the correct one, it should be moved into the wiki. The people to blame is more those who created the tag into OSM without any wiki documentation.</p>
</div>
<div id="comment-32041-info" class="comment-info">
<span class="comment-age">(01 Apr '14, 10:54)</span> <span class="comment-user userinfo">Pieren</span>
</div>
</div>
</div>
<div id="comment-tools-32021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32021-form-container" class="comment-form-container">
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

