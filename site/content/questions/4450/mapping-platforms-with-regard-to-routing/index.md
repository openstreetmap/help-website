+++
type = "question"
title = "mapping platforms with regard to routing"
description = '''When trying to get some walking directions using some OSM routing services all of them failed to route through a bridge specifically marked for pedestrians. (Here is a permalink to the bridge.) Examining the issue it turned out that the problem is NOT with the bridge but with a way marked as highway...'''
date = "2011-04-13T15:32:00Z"
lastmod = "2011-04-14T19:35:00Z"
weight = 4450
keywords = [ "pedestrian", "routing" ]
aliases = [ "/questions/4450" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [mapping platforms with regard to routing](/questions/4450/mapping-platforms-with-regard-to-routing)

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
<span id="post-4450-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4450-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-4450-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>When trying to get some walking directions using some OSM routing services all of them failed to route through a bridge specifically marked for pedestrians. (Here is a <a href="https://www.openstreetmap.org/?lat=47.467064&amp;lon=19.016944&amp;zoom=18&amp;layers=M">permalink</a> to the bridge.)</p>
<p>Examining the issue it turned out that the problem is NOT with the bridge but with a way marked as highway=platform that 'leads' to the bridge. At least the original mapper assumed that the platform will be considered by routing services as something that can be traversed by foot.</p>
<p>I'm not sure what the correct solution to this is. Is it correct to assume that this is a bug in the routing engines (strangely all of them ignore highway=platform)?</p>
<p>Or should I draw a highway=pedestrian beside the platform so that it is obvious that you can pass there?</p>
<p>Wondering what the correct solution is.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-pedestrian" rel="tag" title="see questions tagged &#39;pedestrian&#39;">pedestrian</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Apr '11, 15:32</strong></p>
<img src="https://secure.gravatar.com/avatar/71a7f16e513c7ee5cd9d4230f9127199?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="rizsolt&#39;s gravatar image" />
<p><span>rizsolt</span><br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="rizsolt has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Apr '11, 06:50</strong> </span></p>
</div>
</div>
<div id="comments-container-4450" class="comments-container">
<span id="4452"></span>
<div id="comment-4452" class="comment">
<div id="post-4452-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Besides a general solution about the processing of highway=platform by all known routing engines, can you edit your question and add a permalink to that area where that way is?</p>
</div>
<div id="comment-4452-info" class="comment-info">
<span class="comment-age">(13 Apr '11, 17:09)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="4464"></span>
<div id="comment-4464" class="comment">
<div id="post-4464-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Added the permalink. I don't understand what are you exactly suggesting about the routing engines. Should I open bugs for each of them? Isn't more discussion necessary?</p>
</div>
<div id="comment-4464-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 06:54)</span> <span class="comment-user userinfo">rizsolt</span>
</div>
</div>
<span id="4469"></span>
<div id="comment-4469" class="comment">
<div id="post-4469-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@rizsolt</span>: Of course more discussion ca be helpful about this topic. But IMHO any of the OSM mailing lists or <a href="http://forum.osm.org">http://forum.osm.org</a> is a better place for such a kind of finding solutions for a complex topic like "tagging and routing" ... come over.</p>
</div>
<div id="comment-4469-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 09:56)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="4474"></span>
<div id="comment-4474" class="comment">
<div id="post-4474-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span></span><span>@stephan75</span> I was (and still am) hoping to get a definitive answer on how to map this correctly :)</p>
</div>
<div id="comment-4474-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 11:14)</span> <span class="comment-user userinfo">rizsolt</span>
</div>
</div>
</div>
<div id="comment-tools-4450" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4450-form-container" class="comment-form-container">
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

<span id="4465"></span>

<div id="answer-container-4465" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4465-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4465-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4465-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My advice is to do the same as with the renderers: don't map for routing engines. <a href="https://wiki.openstreetmap.org/wiki/Tag:highway%3Dplatform">highway=platform</a> is a legal way that can be used by passengers. There are lots of tags currently ignored by most routing engines or insufficiently used (like areas). It's a bug that should be reported and not circumvented by mapping an additional, non-existing way.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '11, 07:32</strong></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="scai has 168 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-4465" class="comments-container">
&#10;</div>
<div id="comment-tools-4465" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4465-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4468"></span>

<div id="answer-container-4468" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4468-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4468-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-4468-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I wouldn't necessarily assume that highway=platform implies unfettered pedestrian access. Certainly in the UK, many railway platforms are 'gated' and only offer access to those with valid rail tickets.</p>
<p>If the platform <em>is</em> open to all pedestrians, then you should add an access tag, probably foot=yes or foot=permissive.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Apr '11, 09:32</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-4468" class="comments-container">
<span id="4473"></span>
<div id="comment-4473" class="comment">
<div id="post-4473-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are gated railway platforms here too, but AFAIR railway=platform should be used to tag them.</p>
<p>This particular platform is for a bus stop for public transit, most of those here is free for use by pedestrians altough some of them is not intended to be used as such (usually only if it does not lead anywhere). At this place the platform is just a broadened sidewalk/pavement used for both functions.</p>
<p>I'm not sure if foot=yes is the perfect way to map this...</p>
</div>
<div id="comment-4473-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 11:10)</span> <span class="comment-user userinfo">rizsolt</span>
</div>
</div>
<span id="4495"></span>
<div id="comment-4495" class="comment">
<div id="post-4495-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>There are also tags for gates or other types of barriers and, of course, the well-known access tag.</p>
</div>
<div id="comment-4495-info" class="comment-info">
<span class="comment-age">(14 Apr '11, 19:35)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-4468" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4468-form-container" class="comment-form-container">
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

