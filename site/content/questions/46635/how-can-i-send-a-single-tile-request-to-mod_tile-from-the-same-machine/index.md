+++
type = "question"
title = "How can I send a single tile request to mod_tile from the same machine ?"
description = '''I would like to be able to send single tile requests to mod_tile locally. Ideally, I would like to do this without going through apache since it is a waste of CPU time for my application : the request is coming from the same machine where the tile server is installed and the tiles are used locally. ...'''
date = "2015-11-16T21:53:00Z"
lastmod = "2015-11-17T10:33:00Z"
weight = 46635
keywords = [ "apache", "renderd", "protocol", "mod_tile" ]
aliases = [ "/questions/46635" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I send a single tile request to mod_tile from the same machine ?](/questions/46635/how-can-i-send-a-single-tile-request-to-mod_tile-from-the-same-machine)

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
<span id="post-46635-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46635-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46635-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I would like to be able to send single tile requests to mod_tile locally. Ideally, I would like to do this without going through apache since it is a waste of CPU time for my application : the request is coming from the same machine where the tile server is installed and the tiles are used locally.</p>
<p>From what I understood I can communicate with renderd via a UNIX socket. I'm ok with that, there's no real documentation but since I have access to the source code I think I can create a client socket, send the correct message and receive a reply from renderd.</p>
<p>Before I start implementing anything, I would like to ask if this is the correct way to proceed. I'm only interested in requesting a single tile at a time (meta-tiles are not good for me). If I'm communicating with renderd directly, without going through mod_tile, then this would imply that the tiles would always be rendered without profiting from mod_tile's cache, am I right?</p>
<p>Does mod_tile have a way to receive commands from either the command line or via a socket? Are there any tools available that allow to send a single tile request to mod_tile ? If not, how can I request a single tile from my tile server ?</p>
<p>Thank you for your time.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-apache" rel="tag" title="see questions tagged &#39;apache&#39;">apache</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-protocol" rel="tag" title="see questions tagged &#39;protocol&#39;">protocol</span> <span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Nov '15, 21:53</strong></p>
<img src="https://secure.gravatar.com/avatar/8f0a649a87d1a902597ca226c8080b0f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="kgaitanis&#39;s gravatar image" />
<p><span>kgaitanis</span><br />
<span class="score" title="21 reputation points">21</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="kgaitanis has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Nov '15, 21:56</strong> </span></p>
</div>
</div>
<div id="comments-container-46635" class="comments-container">
&#10;</div>
<div id="comment-tools-46635" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46635-form-container" class="comment-form-container">
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

<span id="46636"></span>

<div id="answer-container-46636" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46636-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46636-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46636-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You should be able to use render_list or at least its code, see: <a href="https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a> bottom of the page.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Nov '15, 22:25</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-46636" class="comments-container">
<span id="46651"></span>
<div id="comment-46651" class="comment">
<div id="post-46651-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for your answer, however render_list generates meta-tiles. I'm interested in single tiles (in .png format). Generating meta-tiles and then extracting a single tile seems a little too long. Isn't there a way to get a single tile?</p>
</div>
<div id="comment-46651-info" class="comment-info">
<span class="comment-age">(17 Nov '15, 09:55)</span> <span class="comment-user userinfo">kgaitanis</span>
</div>
</div>
</div>
<div id="comment-tools-46636" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46636-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46653"></span>

<div id="answer-container-46653" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46653-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Since <code>mod_tile</code> is an Apache module, it's not surprising that requests to mod_tile have to go via Apache.</p>
<p>Renderd generates metatiles on-disk, and doesn't send any image information in response to any requests - it takes a rendering request, puts the metatile on disk, and tells you that the request is complete. While you can take the metatile and decode it to fetch an image, there is a much easier way - just ask mod_tile for the image.</p>
<p>It's possible to set up renderd to use alternate sized metatiles, but I wouldn't recommend it.</p>
<p>I'm intrigued as to what you're rendering. You say that going via mod_tile is a waste of CPU time, but I would guess the overhead is less than 1% compared to the rendering time. Have you measured it? Perhaps you are optimising something that isn't really a problem?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Nov '15, 10:29</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-46653" class="comments-container">
<span id="46654"></span>
<div id="comment-46654" class="comment">
<div id="post-46654-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That's the correct answer : mod_tile is an apache module. I'm just trying to avoid going through the localhost loop but apparently it is not possible. Thanks</p>
</div>
<div id="comment-46654-info" class="comment-info">
<span class="comment-age">(17 Nov '15, 10:33)</span> <span class="comment-user userinfo">kgaitanis</span>
</div>
</div>
</div>
<div id="comment-tools-46653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46653-form-container" class="comment-form-container">
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

