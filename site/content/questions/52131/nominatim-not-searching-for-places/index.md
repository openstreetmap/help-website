+++
type = "question"
title = "Nominatim not searching for places"
description = '''I noticed that Nominatim has strange preference for boundary:administrative over place:XYZ when they have same name. Here is very simple example: https://nominatim.openstreetmap.org/search.php?q=Balzers It returns one result: https://nominatim.openstreetmap.org/details.php?place_id=144926588 Which i...'''
date = "2016-09-20T16:17:00Z"
lastmod = "2016-09-22T22:12:00Z"
weight = 52131
keywords = [ "search", "nominatim", "place" ]
aliases = [ "/questions/52131" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Nominatim not searching for places](/questions/52131/nominatim-not-searching-for-places)

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
<span id="post-52131-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52131-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52131-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I noticed that Nominatim has strange preference for boundary:administrative over place:XYZ when they have same name. Here is very simple example:</p>
<p><a href="https://nominatim.openstreetmap.org/search.php?q=Balzers">https://nominatim.openstreetmap.org/search.php?q=Balzers</a></p>
<p>It returns one result:</p>
<p><a href="https://nominatim.openstreetmap.org/details.php?place_id=144926588">https://nominatim.openstreetmap.org/details.php?place_id=144926588</a></p>
<p>Which is boundary:administrative. In the linked places there is this place:</p>
<p><a href="https://nominatim.openstreetmap.org/details.php?place_id=586113">https://nominatim.openstreetmap.org/details.php?place_id=586113</a></p>
<p>Which is place:village. I am wondering why doesn't it show up in search results. I am personally more interested in places so I am wondering if it is possible to add a parameter to search to prefer places or it is a server-side setting for Nominatim. I have a local instance running as well so I can try to play with that.</p>
<p>Thanks!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-search" rel="tag" title="see questions tagged &#39;search&#39;">search</span> <span class="post-tag tag-link-nominatim" rel="tag" title="see questions tagged &#39;nominatim&#39;">nominatim</span> <span class="post-tag tag-link-place" rel="tag" title="see questions tagged &#39;place&#39;">place</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 Sep '16, 16:17</strong></p>
<img src="https://secure.gravatar.com/avatar/82d3ad1de1b2b52e33ae85a9e396cdeb?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andrey&#39;s gravatar image" />
<p><span>Andrey</span><br />
<span class="score" title="31 reputation points">31</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andrey has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Sep '16, 16:17</strong> </span></p>
</div>
</div>
<div id="comments-container-52131" class="comments-container">
<span id="52178"></span>
<div id="comment-52178" class="comment">
<div id="post-52178-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>meta: In general, please do not post your questions to several places. That wastes help resources. If you really need to (for whatever reason), please always mentioning it in each post and provide links to the other posts. Once you've got an answer at one place, update all the other places.</p>
</div>
<div id="comment-52178-info" class="comment-info">
<span class="comment-age">(22 Sep '16, 20:21)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="52184"></span>
<div id="comment-52184" class="comment">
<div id="post-52184-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> I will note that. It was just not very clear for me whether help.openstreetmap.org and mailing lists are maintained by same community.</p>
</div>
<div id="comment-52184-info" class="comment-info">
<span class="comment-age">(22 Sep '16, 22:12)</span> <span class="comment-user userinfo">Andrey</span>
</div>
</div>
</div>
<div id="comment-tools-52131" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52131-form-container" class="comment-form-container">
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

<span id="52167"></span>

<div id="answer-container-52167" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52167-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52167-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-52167-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="Andrey has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This question got answered on the geocoding mailinglist <a href="https://lists.openstreetmap.org/pipermail/geocoding/2016-September/001823.html">https://lists.openstreetmap.org/pipermail/geocoding/2016-September/001823.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Sep '16, 14:04</strong></p>
<img src="https://secure.gravatar.com/avatar/96aad1e1801b7ea36fba50687924c935?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mtmail&#39;s gravatar image" />
<p><span>mtmail</span><br />
<span class="score" title="4757 reputation points"><span>4.8k</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="74 badges"><span class="bronze">●</span><span class="badgecount">74</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="mtmail has 50 accepted answers">27%</span></p>
</div>
</div>
<div id="comments-container-52167" class="comments-container">
&#10;</div>
<div id="comment-tools-52167" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52167-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52153"></span>

<div id="answer-container-52153" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52153-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52153-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-52153-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As you point out yourself the behaviour is by design (to suppress having two OSM objects and results for the same entity).</p>
<p>You should probably raise the issue wrt specifically searching for places here <a href="https://github.com/twain47/Nominatim">https://github.com/twain47/Nominatim</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '16, 20:56</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Sep '16, 22:07</strong> </span></p>
</div>
</div>
<div id="comments-container-52153" class="comments-container">
<span id="52172"></span>
<div id="comment-52172" class="comment">
<div id="post-52172-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It is strange because sometimes Nominatim has no problem returning same entities: <a href="https://nominatim.openstreetmap.org/search.php?q=weesp&amp;polygon=1&amp;viewbox=">https://nominatim.openstreetmap.org/search.php?q=weesp&amp;polygon=1&amp;viewbox=</a></p>
</div>
<div id="comment-52172-info" class="comment-info">
<span class="comment-age">(22 Sep '16, 19:12)</span> <span class="comment-user userinfo">Andrey</span>
</div>
</div>
<span id="52175"></span>
<div id="comment-52175" class="comment">
<div id="post-52175-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Those are all different entities (suburb, city, motorway junction, etc.), but with the same name.</p>
</div>
<div id="comment-52175-info" class="comment-info">
<span class="comment-age">(22 Sep '16, 19:32)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="52176"></span>
<div id="comment-52176" class="comment">
<div id="post-52176-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/8189/alester">@alester</a> it is very confusing because essentially there is no way to either filter out some results or figure out which administrative levels they represent.</p>
</div>
<div id="comment-52176-info" class="comment-info">
<span class="comment-age">(22 Sep '16, 20:13)</span> <span class="comment-user userinfo">Andrey</span>
</div>
</div>
</div>
<div id="comment-tools-52153" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52153-form-container" class="comment-form-container">
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

