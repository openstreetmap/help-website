+++
type = "question"
title = "How to respond to a fixme (tag) request? Erase or modify?"
description = '''What should I do with a bus stop that has a fixme request? There is a bus stop marked on the map, with a fixme request for status, the bus stop does not exist on the ground. Do I erase the tag or answer the fixme question somehow and leave insitu'''
date = "2012-02-19T19:41:00Z"
lastmod = "2013-06-18T08:30:00Z"
weight = 10661
keywords = [ "fixme" ]
aliases = [ "/questions/10661" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to respond to a fixme (tag) request? Erase or modify?](/questions/10661/how-to-respond-to-a-fixme-tag-request-erase-or-modify)

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
<span id="post-10661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10661-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-10661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>What should I do with a bus stop that has a fixme request? There is a bus stop marked on the map, with a fixme request for status, the bus stop does not exist on the ground. Do I erase the tag or answer the fixme question somehow and leave insitu</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-fixme" rel="tag" title="see questions tagged &#39;fixme&#39;">fixme</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>19 Feb '12, 19:41</strong></p>
<img src="https://secure.gravatar.com/avatar/8619ed34e4b631ab72806814d98aee1a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="tomrobin&#39;s gravatar image" />
<p><span>tomrobin</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="tomrobin has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>18 Jun '13, 01:16</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-10661" class="comments-container">
&#10;</div>
<div id="comment-tools-10661" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10661-form-container" class="comment-form-container">
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

<span id="10664"></span>

<div id="answer-container-10664" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10664-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10664-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-10664-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It could be worth checking the source of the bus stop. Have a look to see if there is any <code>source</code> tag, and check the history to see who added it originally. It may have come from some sort of import, eg in the UK, a lot of bus stops were added by the <a href="http://wiki.openstreetmap.org/wiki/NaPTAN/Import">NaPTAN import</a>.</p>
<p>If it is from the NaPTAN import it should have several naptan tags, and you can follow the guidelines at <a href="http://wiki.openstreetmap.org/wiki/NaPTAN/Surveying_and_Merging_NaPTAN_and_OSM_data">Surveying and merging NaPTAN and OSM data</a>.</p>
<p>Note the NaPTAN data includes a number of bus stops which are not actually physically present on the ground. For these, it is worth checking whether they are actually used as bus stops, ie is there a bus service that stops at that location. If it is used as a bus stop, then you can add the <code>physically_present=no</code> tag, and leave all of the other tags. If it is not used as a bus stop, then you can remove the <code>highway=bus_stop</code> tag.</p>
<p>If the bus stop is not from some sort of import, then you could contact the user who originally added it, and ask about it. And if you are sure that there is no bus stop at that location, its probably best just to delete the bus stop node.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '12, 23:59</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-10664" class="comments-container">
<span id="23476"></span>
<div id="comment-23476" class="comment">
<div id="post-23476-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I suspect it is this bus stop and the one opposite - <a href="http://www.openstreetmap.org/browse/node/1509812105/history">http://www.openstreetmap.org/browse/node/1509812105/history</a> - so not in one particular release of the NaPTAN data, but possible unmarked "customary" stops, which are the hardest to map and/or verify (physically_present=no as Vclaw mentions above).</p>
<p>Edit: If it is those, then the 15/06/2013 NaPTAN data I just downloaded suggests those should be marked bus stops both opposite and adjacent (and known as) War Memorial. <a href="http://www.dft.gov.uk/NaPTAN/snapshot/NaPTANcsv.zip">http://www.dft.gov.uk/NaPTAN/snapshot/NaPTANcsv.zip</a></p>
</div>
<div id="comment-23476-info" class="comment-info">
<span class="comment-age">(18 Jun '13, 08:30)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-10664" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10664-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="10663"></span>

<div id="answer-container-10663" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-10663-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-10663-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-10663-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would erase the tag and would say why in the comment dialog.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Feb '12, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/1fb9da36bbe8817c461df33d395ee413?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gerdami&#39;s gravatar image" />
<p><span>gerdami</span><br />
<span class="score" title="696 reputation points">696</span><span title="27 badges"><span class="badge1">●</span><span class="badgecount">27</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="46 badges"><span class="bronze">●</span><span class="badgecount">46</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gerdami has 2 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-10663" class="comments-container">
&#10;</div>
<div id="comment-tools-10663" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-10663-form-container" class="comment-form-container">
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

