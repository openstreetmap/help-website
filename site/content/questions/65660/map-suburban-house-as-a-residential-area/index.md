+++
type = "question"
title = "Map suburban house as a residential area?"
description = '''Problem I&#x27;m mapping a suburb right now. There are multiple features on each property, like the house, garage, trees, and a shed. How do we map these properties to show that these features belong to the same address? Possible Solution I&#x27;m considering mapping a property as a residential area with an a...'''
date = "2018-08-31T17:49:00Z"
lastmod = "2018-09-03T07:19:00Z"
weight = 65660
keywords = [ "house", "suburb", "property", "relation", "area" ]
aliases = [ "/questions/65660" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Map suburban house as a residential area?](/questions/65660/map-suburban-house-as-a-residential-area)

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
<span id="post-65660-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65660-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65660-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<h2 id="problem">Problem</h2>
<p>I'm mapping a suburb right now. There are multiple features on each property, like the house, garage, trees, and a shed. <strong><em>How do we map these properties to show that these features belong to the same address?</em></strong></p>
<h2 id="possible-solution">Possible Solution</h2>
<p>I'm considering mapping a property as a residential area with an address key, encompassing the house and other features that belong to that address. I've tried mapping the objects together as a relation and it seems like mapping with an area would be much neater. <strong><em>Is this approach kosher?</em></strong></p>
<h3 id="note">Note</h3>
<p>To respect the homeowners' privacy, I'm only mapping features that are visible from the street.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-house" rel="tag" title="see questions tagged &#39;house&#39;">house</span> <span class="post-tag tag-link-suburb" rel="tag" title="see questions tagged &#39;suburb&#39;">suburb</span> <span class="post-tag tag-link-property" rel="tag" title="see questions tagged &#39;property&#39;">property</span> <span class="post-tag tag-link-relation" rel="tag" title="see questions tagged &#39;relation&#39;">relation</span> <span class="post-tag tag-link-area" rel="tag" title="see questions tagged &#39;area&#39;">area</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>31 Aug '18, 17:49</strong></p>
<img src="https://secure.gravatar.com/avatar/bd3e1fb7216c6cf01d6770dcb953256b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="XavierTO&#39;s gravatar image" />
<p><span>XavierTO</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="XavierTO has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-65660" class="comments-container">
&#10;</div>
<div id="comment-tools-65660" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65660-form-container" class="comment-form-container">
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

<span id="65661"></span>

<div id="answer-container-65661" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65661-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65661-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-65661-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="XavierTO has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi XavierTO -- my recommendation would be to simply put address tags on the main house, rather than worrying about tagging the land itself or the outbuildings. It's usually pretty easy to tell visually from the map which outbuildings are associated with which structures.</p>
<p>That said, there's no technical problem that I know of with drawing an area that contains the buildings in question and tagging that area with the address.</p>
<p>No technical problem... but there still may be reasons not to. It's almost always the house itself that is physically decorated with the address in the real world. When you decide that the address belongs to the whole lot, you're making an assumption -- a pretty safe one, but the real world is messy and before long you'll probably run into some iffy cases. A shared garage, an empty lot that may or may not belong to the house next to it, etc.</p>
<p>For ongoing maintenance of the map, it's better to have things tagged in a consistent way rather than in a surprising way. Most mappers will expect to see the address tags on the main houses, and might not even notice them on the areas, which can lead to double-tagging.</p>
<p>Another reason is third-party software compatibility -- many programs that use OSM data are written to expect addresses on buildings and nodes, and may not even recognize different schemes.</p>
<p>In short, simply tagging the main house is 1) good enough 2) much easier than creating an area or a relation 3) less likely to introduce errors of assumption, 4) easier to maintain, and 5) more likely to be compatible with software.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '18, 19:03</strong></p>
<img src="https://secure.gravatar.com/avatar/977d95e2184a885d9a01fb3297225872?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jmapb&#39;s gravatar image" />
<p><span>jmapb</span><br />
<span class="score" title="3387 reputation points"><span>3.4k</span></span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="33 badges"><span class="silver">●</span><span class="badgecount">33</span></span><span title="61 badges"><span class="bronze">●</span><span class="badgecount">61</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jmapb has 22 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Sep '18, 07:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/15d45a99f101e06c9e79916af33f8336?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Privatemajory&#39;s gravatar image" />
<p><span>Privatemajory</span><br />
<span class="score" title="1125 reputation points"><span>1.1k</span></span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="33 badges"><span class="bronze">●</span><span class="badgecount">33</span></span></p>
</div>
</div>
<div id="comments-container-65661" class="comments-container">
<span id="65663"></span>
<div id="comment-65663" class="comment">
<div id="post-65663-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi jmapb - thank you for taking the time to explain these issues. I really appreciate it.</p>
</div>
<div id="comment-65663-info" class="comment-info">
<span class="comment-age">(01 Sep '18, 02:14)</span> <span class="comment-user userinfo">XavierTO</span>
</div>
</div>
<span id="65685"></span>
<div id="comment-65685" class="comment">
<div id="post-65685-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Maybe house numbers being for buildings is a European thing? In Australia they are called street numbers, usually assigned per the cadastral parcel, regardless of if there is a house or not, so in my opinion they should be on the land parcel can be a way with the address, optionally with a landuse tag.</p>
</div>
<div id="comment-65685-info" class="comment-info">
<span class="comment-age">(02 Sep '18, 11:09)</span> <span class="comment-user userinfo">aharvey</span>
</div>
</div>
<span id="65703"></span>
<div id="comment-65703" class="comment">
<div id="post-65703-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/924/harvey">@harvey</a>, depends. House numbers can define an entrance (Italy), parcels, part of buildings/plots, individual flats. BTW, in Denmark and The Netherlands is is recommended to map the housenumber as a point, not on the building outline.</p>
</div>
<div id="comment-65703-info" class="comment-info">
<span class="comment-age">(03 Sep '18, 06:09)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-65661" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65661-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="65662"></span>

<div id="answer-container-65662" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-65662-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-65662-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-65662-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have noticed that many mappers map the fence lines that separate properties and that groups the data visually quite well.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>31 Aug '18, 21:46</strong></p>
<img src="https://secure.gravatar.com/avatar/e5674dd96938593e0af5130dfffe0f90?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nevw&#39;s gravatar image" />
<p><span>nevw</span><br />
<span class="score" title="9843 reputation points"><span>9.8k</span></span><span title="26 badges"><span class="badge1">●</span><span class="badgecount">26</span></span><span title="90 badges"><span class="silver">●</span><span class="badgecount">90</span></span><span title="178 badges"><span class="bronze">●</span><span class="badgecount">178</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nevw has 32 accepted answers">9%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>31 Aug '18, 21:48</strong> </span></p>
</div>
</div>
<div id="comments-container-65662" class="comments-container">
<span id="65664"></span>
<div id="comment-65664" class="comment">
<div id="post-65664-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi nevw - I agree. I've done the same thing and it does separate them quite well.</p>
</div>
<div id="comment-65664-info" class="comment-info">
<span class="comment-age">(01 Sep '18, 02:16)</span> <span class="comment-user userinfo">XavierTO</span>
</div>
</div>
<span id="65704"></span>
<div id="comment-65704" class="comment">
<div id="post-65704-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, and many mappers put the fence line entirely around each property or plot resulting in many duplications of sections of fence.</p>
<p>Further, some mappers also enclose the property or plot by placing fence lines along the party wall of semi-detached properties. Resulting in fence lines through the insides of buildings.</p>
</div>
<div id="comment-65704-info" class="comment-info">
<span class="comment-age">(03 Sep '18, 07:19)</span> <span class="comment-user userinfo">BCNorwich</span>
</div>
</div>
</div>
<div id="comment-tools-65662" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-65662-form-container" class="comment-form-container">
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

