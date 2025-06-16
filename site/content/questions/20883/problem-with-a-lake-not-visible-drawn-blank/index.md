+++
type = "question"
title = "Problem with a lake, not visible, drawn blank"
description = '''Hello, Recently I noticed that one of the lakes in my area is not drawn properly on the standard map - no blue at all, it&#x27;s marked as &quot;meadow&quot; or something. Shows fine in bicycle/transport/mapquest map. This is Anderson Reservoir, in the middle of the map here: https://www.openstreetmap.org/?lat=37.1...'''
date = "2013-03-21T17:45:00Z"
lastmod = "2013-03-24T09:44:00Z"
weight = 20883
keywords = [ "blue", "rendering", "lake", "meadow" ]
aliases = [ "/questions/20883" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Problem with a lake, not visible, drawn blank](/questions/20883/problem-with-a-lake-not-visible-drawn-blank)

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
<span id="post-20883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20883-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-20883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello,</p>
<p>Recently I noticed that one of the lakes in my area is not drawn properly on the standard map - no blue at all, it's marked as "meadow" or something. Shows fine in bicycle/transport/mapquest map. This is Anderson Reservoir, in the middle of the map here:</p>
<p><a href="https://www.openstreetmap.org/?lat=37.1694&amp;lon=-121.6205&amp;zoom=14&amp;layers=M">https://www.openstreetmap.org/?lat=37.1694&amp;lon=-121.6205&amp;zoom=14&amp;layers=M</a></p>
<p>I checked things with JOSM - the lake seems to be a closed polygon, clockwise direction, looks fine to me. There are some complex overlapping polygons that I guess cause the problem, but I don't dare attempt this complex an edit without understanding the problem first. Can somebody more experienced in OSM matters take a look?</p>
<p>Regards,</p>
<ul>
<li>Alex</li>
</ul>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-blue" rel="tag" title="see questions tagged &#39;blue&#39;">blue</span> <span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-lake" rel="tag" title="see questions tagged &#39;lake&#39;">lake</span> <span class="post-tag tag-link-meadow" rel="tag" title="see questions tagged &#39;meadow&#39;">meadow</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Mar '13, 17:45</strong></p>
<img src="https://secure.gravatar.com/avatar/b15bc68887eb3c5049b75e36c6b9c438?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Alexander%20Avtanski&#39;s gravatar image" />
<p><span>Alexander Av...</span><br />
<span class="score" title="46 reputation points">46</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Alexander Avtanski has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20883" class="comments-container">
<span id="20908"></span>
<div id="comment-20908" class="comment">
<div id="post-20908-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks everybody.</p>
<p>I'll first talk to nmixter and if necessary will try fixing the polygons myself (first backing up the data with JOSM).</p>
<p>Thanks,</p>
<ul>
<li>Alex</li>
</ul>
</div>
<div id="comment-20908-info" class="comment-info">
<span class="comment-age">(22 Mar '13, 16:29)</span> <span class="comment-user userinfo">Alexander Av...</span>
</div>
</div>
</div>
<div id="comment-tools-20883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20883-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="20900"></span>

<div id="answer-container-20900" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20900-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20900-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-20900-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Yes, the rendering problems are caused by several areas which are overlapping with the lake.</p>
<p>Most of the lake is covered by this area, for Anderson Lake County Park: <a href="https://www.openstreetmap.org/browse/way/28461629">way 28461629</a>. This is tagged as <code>leisure=park</code> - this area may be a "county park", but it seems it doesn't meet the OSM definition for <code>leisure=park</code>, ie "open, green area for recreation". It should probably be tagged with <code>boundary=national_park</code> or <code>boundary=protected_area</code> instead.</p>
<p>Also the lake is surrounded by a way which is an outer part of <a href="https://www.openstreetmap.org/browse/relation/1696825">relation 1696825</a>. This relation is tagged as <code>landuse=meadow</code>. The lake doesn't meet the OSM defintion of meadow "land primarily vegetated by grass plus other non-woody plants", so shouldn't be tagged as that. It appears that relation is from an import of government data for farmland.</p>
<p>It would be worth contacting the user who originally added this (nmixter), or discussing it on the talk-us mailing list, to agree how these areas should be mapped and tagged.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '13, 13:24</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-20900" class="comments-container">
&#10;</div>
<div id="comment-tools-20900" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20900-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20885"></span>

<div id="answer-container-20885" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20885-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20885-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20885-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have just compared the mapping (in PotLatch2) of your lake with the mapping of Coyote Reservoir which is to the South East. The only difference is that Coyote Reservoir has a Multipolygon relation, with an ID and Role is set as Outer (Ditto this for Lake Windemere, Cumbria, UK) whereas Anderson Reservoir appears to have this Relation missing. Not sure if this is a solution or not.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Mar '13, 19:27</strong></p>
<img src="https://secure.gravatar.com/avatar/880b2e6608677d0d2bf800aeea5c922d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AliOnHols&#39;s gravatar image" />
<p><span>AliOnHols</span><br />
<span class="score" title="56 reputation points">56</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AliOnHols has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-20885" class="comments-container">
&#10;</div>
<div id="comment-tools-20885" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20885-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20886"></span>

<div id="answer-container-20886" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20886-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20886-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-20886-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi the Anderson lake should be tagged as inner polygon inside the leisure park just to appear properly now it seems the be partly green park. The Coyote lake is partly a 2 (broken) multipolygon and should be tagged inner (natural water) and outer (park) in the advanced menu P2. What’s the use of the thin line (multipolygon with 95 others) following the waterline more or less ? Whats the main outer polygon ? Or just ask the editor nmixter why it has be done ? By sending the last editor a simple mail with your remarks. It might get you an answer as well ! And MK 408 as well for the southern lake. You can find or identify the editor by using the button H if the node or nodes are marked. In JOSM its on the right in the scrolling menus. Greetz</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Mar '13, 20:26</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-20886" class="comments-container">
<span id="20898"></span>
<div id="comment-20898" class="comment">
<div id="post-20898-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Should the outer polygon totally contain the inner one? which it doesn't in this case as we can see the white area on the map. If only half the lake is in the park should the lake be in two sections? good point about contacting mapper. Maybe part of blank polygon could be used take the park polygon around the edge on the lake??</p>
</div>
<div id="comment-20898-info" class="comment-info">
<span class="comment-age">(22 Mar '13, 12:22)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-20886" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20886-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="20896"></span>

<div id="answer-container-20896" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-20896-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20896-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20896-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><img src="/upfiles/blank_polygon.JPG" alt="alt text" />There appears to be two polygons around the lake one tagged lake the other without any tags,which I think may be the problem. I would be reluctant to delete the blank one as it would been difficult to re-do. I use potlatch2 but I believe it is easier to retain the polygon on your PC to put back if necessary if you are using JOSM. Hopefully a more experienced mapper will know the safe procedure. here is the blank polygon.<br />
</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>22 Mar '13, 11:14</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span> </br></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>22 Mar '13, 11:20</strong> </span></p>
</div>
</div>
<div id="comments-container-20896" class="comments-container">
<span id="20945"></span>
<div id="comment-20945" class="comment">
<div id="post-20945-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I certainly wouldn't delete the untagged way - you can see in that screenshot that it's part of a multipolygon relation!</p>
</div>
<div id="comment-20945-info" class="comment-info">
<span class="comment-age">(24 Mar '13, 09:05)</span> <span class="comment-user userinfo">Andy Allan</span>
</div>
</div>
<span id="20946"></span>
<div id="comment-20946" class="comment">
<div id="post-20946-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Additionally ways without tags and without being member of any relation are rarely a problem, if ever.</p>
</div>
<div id="comment-20946-info" class="comment-info">
<span class="comment-age">(24 Mar '13, 09:44)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-20896" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20896-form-container" class="comment-form-container">
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

