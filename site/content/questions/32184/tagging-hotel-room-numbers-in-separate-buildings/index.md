+++
type = "question"
title = "Tagging hotel room numbers in separate buildings"
description = '''In Furnace Creek Ranch, Death Valley, there are some hotel rooms which are in separate cabins, 2 rooms per cabin. They are numbered, 201 on up. The number is not attached to a street. One options is to use addr:housenumber to record the number. The number shows up nicely in maps, but there are warni...'''
date = "2014-04-08T00:38:00Z"
lastmod = "2014-04-17T19:53:00Z"
weight = 32184
keywords = [ "hotel", "room", "number" ]
aliases = [ "/questions/32184" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Tagging hotel room numbers in separate buildings](/questions/32184/tagging-hotel-room-numbers-in-separate-buildings)

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
<span id="post-32184-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32184-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32184-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In Furnace Creek Ranch, Death Valley, there are some hotel rooms which are in separate cabins, 2 rooms per cabin. They are numbered, 201 on up. The number is not attached to a street.</p>
<p>One options is to use addr:housenumber to record the number. The number shows up nicely in maps, but there are warnings about not having a street name to go with the house number.</p>
<p>Here is a view of the area.</p>
<p><a href="http://www.openstreetmap.org/#map=19/36.45764/-116.86580">http://www.openstreetmap.org/#map=19/36.45764/-116.86580</a></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-hotel" rel="tag" title="see questions tagged &#39;hotel&#39;">hotel</span> <span class="post-tag tag-link-room" rel="tag" title="see questions tagged &#39;room&#39;">room</span> <span class="post-tag tag-link-number" rel="tag" title="see questions tagged &#39;number&#39;">number</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 Apr '14, 00:38</strong></p>
<img src="https://secure.gravatar.com/avatar/96cceebb21bf8e94d09c377653972afd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nereocystis&#39;s gravatar image" />
<p><span>nereocystis</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nereocystis has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-32184" class="comments-container">
&#10;</div>
<div id="comment-tools-32184" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32184-form-container" class="comment-form-container">
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

<span id="32194"></span>

<div id="answer-container-32194" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32194-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32194-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-32194-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please do not use <code>addr:housenumber</code> for hotel rooms, even if they are located in different buildings and they show up on the map. Using this tag in this way will cause issues for tools which search for valid addresses. It will create noise.</p>
<p>Hotel rooms are subsidiary elements at a '''single''' address and therefore should be tagged as such. Similar elements which are in use are addr:suite (for office suites within a building or complex) and <code>addr:flats</code> (for flats and apartments within a building or complex).</p>
<p>By analogy you could use a tag <code>addr:hotel_roomnumber</code> or similar for this case, although, personally I'm uncertain as to whether this is appropriate information for OSM.</p>
<p>Also OSM has a principle of <a href="http://wiki.openstreetmap.org/wiki/One_feature,_one_OSM_element">one feature one element</a>, currently this resort appears to be mapped as multiple hotels. It would be better if this was mapped as an area enclosing the various buildings.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '14, 11:07</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-32194" class="comments-container">
<span id="32225"></span>
<div id="comment-32225" class="comment">
<div id="post-32225-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks.</p>
<p>This looks like some good ideas. To me, suite seems like the best bet. Since the buildings are separate, with separate number, I think that it is appropriate. I would probably skip hotel_roomnumber, since it is not otherwise used.</p>
<p>It might be appropriate to use multi_polygon for the various buildings. Area doesn't work as well. The building are scattered around the property, with other buildings and stores in between. However, this group could be set up as an area. I'll have to look at a practical way of handling it.</p>
</div>
<div id="comment-32225-info" class="comment-info">
<span class="comment-age">(09 Apr '14, 15:44)</span> <span class="comment-user userinfo">nereocystis</span>
</div>
</div>
<span id="32263"></span>
<div id="comment-32263" class="comment">
<div id="post-32263-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Use amenity=hotel for the whole area, map the buildings separately no need for a multi-polygon anywhere. The room numbers are not house numbers therefore if you continue to use this key you are 'tagging for the renderer'. If there is a house which shares the number of a room on the same road you will confuse search engines.</p>
</div>
<div id="comment-32263-info" class="comment-info">
<span class="comment-age">(10 Apr '14, 11:03)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="32417"></span>
<div id="comment-32417" class="comment">
<div id="post-32417-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks.</p>
<p>I used tourism=hotel for a new area around the individual buildings, and for for the individual buildings, use as building=yes. Unfortunately, building=hotel is rendered by the rendering engines. I assume that the rendering engines use multiple methods of determining whether something should be rendered as a hotel.</p>
<p>And I used addr:suite for the individual units. This seems like a moderately well-used tag which is a close match for this purpose.</p>
</div>
<div id="comment-32417-info" class="comment-info">
<span class="comment-age">(17 Apr '14, 19:53)</span> <span class="comment-user userinfo">nereocystis</span>
</div>
</div>
</div>
<div id="comment-tools-32194" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32194-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="32185"></span>

<div id="answer-container-32185" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-32185-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-32185-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-32185-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, use the street address of the main hotel building and add the separated numbers to it, to locate the other buildings or rooms. It looks like if I’m not mistaken that the street in between has a name tag as Date Grove Road.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Apr '14, 01:22</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-32185" class="comments-container">
<span id="32214"></span>
<div id="comment-32214" class="comment">
<div id="post-32214-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The street name will be corrected soon, as that is not the actual street name. Another problem.</p>
</div>
<div id="comment-32214-info" class="comment-info">
<span class="comment-age">(09 Apr '14, 01:58)</span> <span class="comment-user userinfo">nereocystis</span>
</div>
</div>
</div>
<div id="comment-tools-32185" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-32185-form-container" class="comment-form-container">
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

