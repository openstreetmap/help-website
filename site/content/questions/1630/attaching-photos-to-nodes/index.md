+++
type = "question"
title = "Attaching photos to nodes"
description = '''I&#x27;m trying to attach a photo to one node,  but in all the solutions I got they explain how to attach one route nodes to the pictures taken while doing that route, what I think is named georeferencing (like in this video). This is not what I mean. What I&#x27;m really looking for is how to create a node i...'''
date = "2010-11-25T10:19:00Z"
lastmod = "2013-12-10T09:24:00Z"
weight = 1630
keywords = [ "photos", "mapping" ]
aliases = [ "/questions/1630" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [Attaching photos to nodes](/questions/1630/attaching-photos-to-nodes)

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
<span id="post-1630-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1630-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-1630-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm trying to attach a photo to one node,</p>
<p>but in all the solutions I got they explain how to attach one route nodes to the pictures taken while doing that route, what I think is named georeferencing (like in <a href="http://showmedo.com/videotutorials/video?name=1800040&amp;fromSeriesID=180">this video</a>). This is not what I mean.</p>
<p>What I'm really looking for is how to create a node in the map (in an area that I already know) and then attach one picture to that node, so in case someone click on it, the photo gets enlarged.</p>
<p>Does anybody have any idea?</p>
<p>Thank you all!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-photos" rel="tag" title="see questions tagged &#39;photos&#39;">photos</span> <span class="post-tag tag-link-mapping" rel="tag" title="see questions tagged &#39;mapping&#39;">mapping</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Nov '10, 10:19</strong></p>
<img src="https://secure.gravatar.com/avatar/51ff385f784b84eb8edc38b932e877aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Stackhouse&#39;s gravatar image" />
<p><span>Stackhouse</span><br />
<span class="score" title="60 reputation points">60</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Stackhouse has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Dec '13, 12:09</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-1630" class="comments-container">
&#10;</div>
<div id="comment-tools-1630" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1630-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="1634"></span>

<div id="answer-container-1634" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1634-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-1634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM does not store photo data. One approach is to store photos on an external site like Flickr, then create a mashup view which combines both databases. An example is the "Wikipedia links" map, which has live links to Flickr photos: <a href="http://www.openstreetmap.pl/wp/?lat=51.2592412&amp;lon=-2.1832964&amp;zoom=17">http://www.openstreetmap.pl/wp/?lat=51.2592412&amp;lon=-2.1832964&amp;zoom=17</a> . Note that I don't believe the Flickr links on this map are updated, so any future Flickr uploads with OSM tags won't appear on this map. You would need to use something like OpenLayers and some sort of extra processing to create this sort of map. Note that the "Wikipedia Links" map example only runs on the FireFox browser.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '10, 12:14</strong></p>
<img src="https://secure.gravatar.com/avatar/1dd5f61a81b99dd54ec6f33d96aa38b2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Mike%20N&#39;s gravatar image" />
<p><span>Mike N</span><br />
<span class="score" title="2926 reputation points"><span>2.9k</span></span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="22 badges"><span class="silver">●</span><span class="badgecount">22</span></span><span title="54 badges"><span class="bronze">●</span><span class="badgecount">54</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Mike N has 16 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-1634" class="comments-container">
<span id="1646"></span>
<div id="comment-1646" class="comment">
<div id="post-1646-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Mike. I'll try it in that way. Sorry for my previous comment, I hadn´t seen Mike's reply.</p>
</div>
<div id="comment-1646-info" class="comment-info">
<span class="comment-age">(26 Nov '10, 07:32)</span> <span class="comment-user userinfo">Stackhouse</span>
</div>
</div>
</div>
<div id="comment-tools-1634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1634-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="1631"></span>

<div id="answer-container-1631" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-1631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-1631-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-1631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>OSM does not store images in the database, and it probably never will. What you are linking to is a guide to <a href="http://wiki.openstreetmap.org/wiki/Photo_mapping">photomapping</a> witch is a technique for remembering details when mapping.</p>
<p>You might want to look at the project <a href="http://wiki.openstreetmap.org/wiki/OpenStreetView">OpenStreetView</a> witch might give you what you want.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Nov '10, 10:38</strong></p>
<img src="https://secure.gravatar.com/avatar/44a4438f0146dfd898e24c221fd28b58?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Gnonthgol&#39;s gravatar image" />
<p><span>Gnonthgol ♦</span><br />
<span class="score" title="13750 reputation points"><span>13.8k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="103 badges"><span class="silver">●</span><span class="badgecount">103</span></span><span title="198 badges"><span class="bronze">●</span><span class="badgecount">198</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Gnonthgol has 57 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-1631" class="comments-container">
<span id="1632"></span>
<div id="comment-1632" class="comment">
<div id="post-1632-score" class="comment-score">
-1
</div>
<div class="comment-text">
<p>Thanks Gnonthgol. This might help, it seems it has no a lot of options to manage with the pictures though, at least from the web site.</p>
<p>The whole thing I'm trying to do is setting some points in one map (lets say showed by little flags) and then when you click on the flag, get the picture taken in that location. It would be something similar to what they do in Google maps when you click in the balloons with letters.</p>
<p>If anybody have any idea about how to do it or how OpenStreetView could help, I would be grateful for the info.</p>
<p>Thanks in advance!</p>
</div>
<div id="comment-1632-info" class="comment-info">
<span class="comment-age">(25 Nov '10, 11:02)</span> <span class="comment-user userinfo">Stackhouse</span>
</div>
</div>
</div>
<div id="comment-tools-1631" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-1631-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="28949"></span>

<div id="answer-container-28949" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-28949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-28949-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-28949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use a <span>tag</span> with the <span><code>image</code></span> key to specify a link to a photo (or a page where also its license is mentioned …) of a mapped object. Please also see the (there) linked proposal and its talk page.</p>
<p>Note that this tag may not get used by many maps/applications (although surely some). See <a href="http://taginfo.openstreetmap.org/keys/?key=image#values">taginfo</a> (note that there are many pages and that most images are likely uniquely used, so you have to skip many pages to see the mass of use).</p>
<p>If you would like to discuss a new project the proposal page (or a new one?), mailing list <span>or</span> forum would be good to use.</p>
<p>Maybe the <span><code>wikipedia</code></span> key is also interesting for you (could be more useful than just an image). Used, apparently, (also to show photos) by <a href="http://www.openlinkmap.org/?lat=50.113195299999994&amp;lon=8.679413399999993&amp;zoom=16&amp;id=28426081&amp;type=way">OpenLinkMap</a> (unfortunately, does not use the image key).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Dec '13, 09:24</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Dec '13, 12:23</strong> </span></p>
</div>
</div>
<div id="comments-container-28949" class="comments-container">
&#10;</div>
<div id="comment-tools-28949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-28949-form-container" class="comment-form-container">
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

