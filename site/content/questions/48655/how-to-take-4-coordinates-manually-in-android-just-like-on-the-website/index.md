+++
type = "question"
title = "How to take 4 coordinates manually in android just like on the website ?"
description = '''I want to create an app using osm and i want to pick up the coordinates manually from android and then send them to my web service where i download the data of that selected region and apply my algorithm on it. How can i create do that?'''
date = "2016-03-14T18:09:00Z"
lastmod = "2016-03-14T22:45:00Z"
weight = 48655
keywords = [ "development", "android", "webservices" ]
aliases = [ "/questions/48655" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to take 4 coordinates manually in android just like on the website ?](/questions/48655/how-to-take-4-coordinates-manually-in-android-just-like-on-the-website)

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
<span id="post-48655-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-48655-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-48655-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I want to create an app using osm and i want to pick up the coordinates manually from android and then send them to my web service where i download the data of that selected region and apply my algorithm on it. How can i create do that?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-development" rel="tag" title="see questions tagged &#39;development&#39;">development</span> <span class="post-tag tag-link-android" rel="tag" title="see questions tagged &#39;android&#39;">android</span> <span class="post-tag tag-link-webservices" rel="tag" title="see questions tagged &#39;webservices&#39;">webservices</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Mar '16, 18:09</strong></p>
<img src="https://secure.gravatar.com/avatar/260680ff58506528c6e2a8830a9f5d61?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="PopaPetru&#39;s gravatar image" />
<p><span>PopaPetru</span><br />
<span class="score" title="26 reputation points">26</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="PopaPetru has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Mar '16, 21:54</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-48655" class="comments-container">
<span id="48658"></span>
<div id="comment-48658" class="comment">
<div id="post-48658-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>eh, what? Sorry, please describe that with much more words. Also please explain what you already know about OSM and what specifically your problem is.</p>
</div>
<div id="comment-48658-info" class="comment-info">
<span class="comment-age">(14 Mar '16, 20:05)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="48666"></span>
<div id="comment-48666" class="comment">
<div id="post-48666-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>So I want to create a patrolling app of a neighbourhood.I know how do parse osm data and how to download it...that's on the server side. What i don't know is how to let the client(android side) to choose the coordinates of the area he want's to patroll...si i need something like on the osm site where i can manually export some rectangle on the map. I want the client to be able to select that rectangle. And after that how to draw on it the path I calculate on the server side. Thanks for much for the response.</p>
</div>
<div id="comment-48666-info" class="comment-info">
<span class="comment-age">(14 Mar '16, 21:21)</span> <span class="comment-user userinfo">PopaPetru</span>
</div>
</div>
<span id="48668"></span>
<div id="comment-48668" class="comment">
<div id="post-48668-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>so you want to know a Android map framework (for your Android app) which offers you some input like if you click "Manually select a different area" at <a href="https://www.openstreetmap.org/export">https://www.openstreetmap.org/export</a> and you want to display some poly-line on a map like the blue line in <a href="http://umap.openstreetmap.fr/de/map/unbenannte-karte_76136#10/52.4690/13.4122">http://umap.openstreetmap.fr/de/map/unbenannte-karte_76136#10/52.4690/13.4122</a> , right?</p>
</div>
<div id="comment-48668-info" class="comment-info">
<span class="comment-age">(14 Mar '16, 21:51)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="48671"></span>
<div id="comment-48671" class="comment">
<div id="post-48671-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes.And the poly-line could be with arrows :D but i will deal with that when i get there. Can you help me?</p>
</div>
<div id="comment-48671-info" class="comment-info">
<span class="comment-age">(14 Mar '16, 22:37)</span> <span class="comment-user userinfo">PopaPetru</span>
</div>
</div>
<span id="48672"></span>
<div id="comment-48672" class="comment">
<div id="post-48672-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>no, sorry, I am not really an Android dev, but I hope I could help to clarify your question. The only advise I could give is to look at the frameworks which are used by the open source <a href="https://wiki.openstreetmap.org/wiki/Android">Android apps</a>. Just wait some days, others may help here!</p>
</div>
<div id="comment-48672-info" class="comment-info">
<span class="comment-age">(14 Mar '16, 22:43)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="48673"></span>
<div id="comment-48673" class="comment not_top_scorer">
<div id="post-48673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much for your time.</p>
</div>
<div id="comment-48673-info" class="comment-info">
<span class="comment-age">(14 Mar '16, 22:45)</span> <span class="comment-user userinfo">PopaPetru</span>
</div>
</div>
</div>
<div id="comment-tools-48655" class="comment-tools">
<span class="comments-showing"> showing 5 of 6 </span> <a href="#" class="show-all-comments-link">show 1 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-48655-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

