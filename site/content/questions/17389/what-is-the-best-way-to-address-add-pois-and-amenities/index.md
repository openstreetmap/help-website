+++
type = "question"
title = "What is the best way to address / add POIs and Amenities?"
description = '''I have been looking in Germany and other &quot;Example&quot; countries, and still have not found a definitive answer. Some people put the Tags on the building polygon some put it on the area polygon when available. Some add the tags to a entrance node to the building and some add the tags to a node and move i...'''
date = "2012-11-02T00:52:00Z"
lastmod = "2012-11-03T05:39:00Z"
weight = 17389
keywords = [ "addressing", "amenity", "example", "tagging", "poi" ]
aliases = [ "/questions/17389" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [What is the best way to address / add POIs and Amenities?](/questions/17389/what-is-the-best-way-to-address-add-pois-and-amenities)

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
<span id="post-17389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17389-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-17389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I have been looking in Germany and other "Example" countries, and still have not found a definitive answer. Some people put the Tags on the building polygon some put it on the area polygon when available. Some add the tags to a entrance node to the building and some add the tags to a node and move it to the center of the building while some move it near the entrance.</p>
<p>Which way helps OSM the most and is the most useful way to tag them. I already know to use the addr: tags instead of relations since it is quicker to parse and use. Please chime in and give your case for the best way to tag. I want to start adding addresses and Store POIs in commercial districts and would like some solid advice.<br />
</p>
<p><a href="https://www.openstreetmap.org/?lat=41.20145693421364&amp;lon=-73.20170044898987&amp;zoom=18">Here is an example of a Hospital I fixed up.</a> And this is <a href="https://www.openstreetmap.org/?lat=41.17583245038986&amp;lon=-73.22762131690979&amp;zoom=18">an area I would like to add more POIs and make more consistent</a>. Please give me any helpful suggestions.<br />
</p>
<p>Also are there any good examples you could link to, because that would be great. I like learning by examining great examples. P.S. I am not that fond of relations but can do them if need be, I really want the best for this project.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-addressing" rel="tag" title="see questions tagged &#39;addressing&#39;">addressing</span> <span class="post-tag tag-link-amenity" rel="tag" title="see questions tagged &#39;amenity&#39;">amenity</span> <span class="post-tag tag-link-example" rel="tag" title="see questions tagged &#39;example&#39;">example</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 Nov '12, 00:52</strong></p>
<img src="https://secure.gravatar.com/avatar/602a4908e9bea5a3f086bd91654717c4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="redsteakraw&#39;s gravatar image" />
<p><span>redsteakraw</span><br />
<span class="score" title="1040 reputation points"><span>1.0k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="37 badges"><span class="bronze">●</span><span class="badgecount">37</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="redsteakraw has 2 accepted answers">22%</span> </br></br></p>
</div>
</div>
<div id="comments-container-17389" class="comments-container">
&#10;</div>
<div id="comment-tools-17389" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17389-form-container" class="comment-form-container">
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

<span id="17391"></span>

<div id="answer-container-17391" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-17391-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-17391-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-17391-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>My POV of Best Practice:<br />
Nodes are the easiest and fastest way to map a POI. If a user knows details of a POI but not the outline of the building and no imagery is available it is the most logic thing to use.</p>
<p>When there is a way for the building, put the data on the way. Don't add the data to a node and the way. This kind of redundancy is not wanted.</p>
<p>Exceptions: When the building contains multiple POI you can<br />
a) put the POI data on the node for the entrance which leads to the POI in real life or, if that isn't possible<br />
b) just add the POI data to a node inside the building.<br />
</p>
<p>For relations: It is mostly discouraged using them. They break quite easily and are hard to restore. Also I map quite a lot but have seen only ten (or so) of them. Additionally: At least I haven't heard of any tools checking for address relations. So maybe you put a lot of work into them but they will hardly get used.</p>
<p>hth<br />
malenki</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>02 Nov '12, 02:05</strong></p>
<img src="https://secure.gravatar.com/avatar/a18e2b8eb41515c09bb66159941584bf?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="malenki&#39;s gravatar image" />
<p><span>malenki</span><br />
<span class="score" title="4713 reputation points"><span>4.7k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="46 badges"><span class="silver">●</span><span class="badgecount">46</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="malenki has 10 accepted answers">6%</span> </br></br></p>
</div>
</div>
<div id="comments-container-17391" class="comments-container">
<span id="17393"></span>
<div id="comment-17393" class="comment">
<div id="post-17393-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have used relations for buildings with courtyards, also for areas that are related yet non physically next to each other. It is a pain which is why I don't like to use them. It is only slightly easier if I use Merkaartor and start from scratch.</p>
</div>
<div id="comment-17393-info" class="comment-info">
<span class="comment-age">(02 Nov '12, 03:17)</span> <span class="comment-user userinfo">redsteakraw</span>
</div>
</div>
<span id="17396"></span>
<div id="comment-17396" class="comment">
<div id="post-17396-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Re: relations. I guess it depends where you map. associatedStreet relations is what we locally decided what is easier to map, and they are supported by nominatim. We have roughly 1500+ in a fairly rural area of about 300 square km (currently 1805 relations for an area extract, but there are a few multipolygons and boundaries in there too).</p>
</div>
<div id="comment-17396-info" class="comment-info">
<span class="comment-age">(02 Nov '12, 09:07)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="17436"></span>
<div id="comment-17436" class="comment">
<div id="post-17436-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>We locally decided to standardize on addr:street and removed the few associatedStreet relations I had created before because they added unnecessary complexity and served no useful purpose.</p>
<p>Using addr:street, combined with editor presets, makes a common beginner task - adding or correcting an address - as easy as "click on the building, notice the 'address' dialog, type in the house number and street name in those text boxes." I fail to understand how associatedStreet could be considered <em>easier</em> than that.</p>
</div>
<div id="comment-17436-info" class="comment-info">
<span class="comment-age">(03 Nov '12, 05:39)</span> <span class="comment-user userinfo">Tordanik</span>
</div>
</div>
</div>
<div id="comment-tools-17391" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-17391-form-container" class="comment-form-container">
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

