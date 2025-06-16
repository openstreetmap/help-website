+++
type = "question"
title = "Getting watershed from OpenStreetMap"
description = '''Hi, I am Olosunde Ayooluwa, pls I want to ask if I can get the water shed of an area fron OpenStreetMap.'''
date = "2016-11-14T19:28:00Z"
lastmod = "2016-12-08T16:38:00Z"
weight = 52947
keywords = [ "waterbody" ]
aliases = [ "/questions/52947" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Getting watershed from OpenStreetMap](/questions/52947/getting-watershed-from-openstreetmap)

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
<span id="post-52947-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52947-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-52947-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I am Olosunde Ayooluwa, pls I want to ask if I can get the water shed of an area fron OpenStreetMap.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-waterbody" rel="tag" title="see questions tagged &#39;waterbody&#39;">waterbody</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>14 Nov '16, 19:28</strong></p>
<img src="https://secure.gravatar.com/avatar/f92a85aa57084eaba22c87495d809cbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="AYOOLUWA&#39;s gravatar image" />
<p><span>AYOOLUWA</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="AYOOLUWA has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Nov '16, 10:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span></p>
</div>
</div>
<div id="comments-container-52947" class="comments-container">
<span id="52959"></span>
<div id="comment-52959" class="comment">
<div id="post-52959-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What is a "water shed"? What is "get" for you? Do you need some special format? And: is the "water shed" showing up on some map (is it in out data)? Could you please link to some example location? Are you looking for a map like that <a href="http://www.kompf.de/gps/rivermap.html">http://www.kompf.de/gps/rivermap.html</a> (central Europe only)?</p>
</div>
<div id="comment-52959-info" class="comment-info">
<span class="comment-age">(14 Nov '16, 23:09)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-52947" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52947-form-container" class="comment-form-container">
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

<span id="52960"></span>

<div id="answer-container-52960" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52960-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52960-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-52960-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'd have to infer watershed data - it's not something stored in OSM normally.</p>
<p>Rivers and streams are directional in OSM - the direction of the ways should be downstream, and they join other streams on the way to their destination (usually the sea). You can therefore work out where watersheds are by looking at which streams and rivers are connected indirectly to which seas, and drawing the watershed between them.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '16, 23:52</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-52960" class="comments-container">
&#10;</div>
<div id="comment-tools-52960" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52960-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53350"></span>

<div id="answer-container-53350" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53350-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53350-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-53350-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A few rivers like <a href="https://www.openstreetmap.org/relation/192359">River Ob</a> have watersheds in super-relations, but for most rivers there are not any data.</p>
<p>To find out a watershed, you need to get all ways of the relation of the primary outflow river. Then search for nodes with intersections with that river. Get the river up to the source then you will get the final data for a watershed.</p>
<p>By the way, watersheds are usually clearly visible in the cycling map as it is just the ridge of a mountain, except for some borders like the one between <a href="">the Dnieper</a> and <a href="">the Don</a>, which are both located on the Eastern European Plain.</p>
<p><a href="https://www.openstreetmap.org/relation/2086905">https://www.openstreetmap.org/relation/2086905</a> <a href="https://www.openstreetmap.org/relation/416351">https://www.openstreetmap.org/relation/416351</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '16, 09:17</strong></p>
<img src="https://secure.gravatar.com/avatar/100f8ccde5e9799707a5056f94fe183f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wetitpig0&#39;s gravatar image" />
<p><span>Wetitpig0</span><br />
<span class="score" title="307 reputation points">307</span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="19 badges"><span class="silver">●</span><span class="badgecount">19</span></span><span title="28 badges"><span class="bronze">●</span><span class="badgecount">28</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wetitpig0 has 2 accepted answers">10%</span></p>
</div>
</div>
<div id="comments-container-53350" class="comments-container">
&#10;</div>
<div id="comment-tools-53350" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53350-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="53375"></span>

<div id="answer-container-53375" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53375-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53375-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53375-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>These contours should help <a href="http://www.opendem.info/download_contours.html">http://www.opendem.info/download_contours.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>08 Dec '16, 11:36</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
</div>
<div id="comments-container-53375" class="comments-container">
<span id="53380"></span>
<div id="comment-53380" class="comment">
<div id="post-53380-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>How? Do they really show watershed borders or just contour lines? If just contour lines then no use because sometimes the watershed borders are very insignificant.</p>
</div>
<div id="comment-53380-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 14:40)</span> <span class="comment-user userinfo">Wetitpig0</span>
</div>
</div>
<span id="53385"></span>
<div id="comment-53385" class="comment">
<div id="post-53385-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>They help narrow the location of the ridge or watershed line don't they?</p>
</div>
<div id="comment-53385-info" class="comment-info">
<span class="comment-age">(08 Dec '16, 16:38)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-53375" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53375-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="52953"></span>

<div id="answer-container-52953" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-52953-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-52953-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-52953-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, have a look at the plateau de Langres, with 5 France rivers flowing in all directions its a water shed or simple a good water source for rivers. Like the Marne &amp; Seine go west, La Saone goes south, Meuse and Meurthe go north. but no sign of a water shed on the standard OSM map.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '16, 22:19</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-52953" class="comments-container">
&#10;</div>
<div id="comment-tools-52953" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-52953-form-container" class="comment-form-container">
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

