+++
type = "question"
title = "Help about undoing changes and drawing bus routes."
description = '''Good night. As of now, I&#x27;m using Potlach 2 to try to draw bus routes. While learning how to use the tool, I thought I had to add manually the relations (using the Ctrl-R hotkey to repeat the last relation, which has some bugs) to draw the route, not knowing that using the cursor to draw is just enou...'''
date = "2016-05-20T00:45:00Z"
lastmod = "2016-05-21T10:13:00Z"
weight = 49749
keywords = [ "brazil", "bus", "route", "changes", "undo" ]
aliases = [ "/questions/49749" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Help about undoing changes and drawing bus routes.](/questions/49749/help-about-undoing-changes-and-drawing-bus-routes)

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
<span id="post-49749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49749-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Good night. As of now, I'm using Potlach 2 to try to draw bus routes. While learning how to use the tool, I thought I had to add manually the relations (using the Ctrl-R hotkey to repeat the last relation, which has some bugs) to draw the route, not knowing that using the cursor to draw is just enough to add the nodes to the route, as I checked later when trying to extract the data via Overpass Turbo.</p>
<p>However, today, I notice that due to some accident, I've changed some routes that use the same ways, and as a result, I want to, if possible, to undo all my changes done by me in the last, as of this writing, 24 hours. I suppose there won't be much problem in doing so since there seems to be very little activity in my city (Foz do Iguaçu, PR, Brazil), and deleting routes don't seem to do the trick.</p>
<p>I suppose the problem started with accidental misuse of Potlach's features. I probably copied the relations of a node leaving the central bus hub, which had many bus routes associated with it, and even when I realized that mistake, there's also the way Potlach draws routes - You automatically get a cursor from the last point in the route, and at some point I probably got a loose end with several routes attached to it.</p>
<p>Relations 3586878, 3586977 and 3587121, the very few bus routes we had tracked beforehand now are "damaged" by my sloppy job, I just wanted to be able to undo my changes on them, I'm fine with deleting the other two routes I did before and doing them more carefully.</p>
<p>[EDIT]: Upon closer inspection, it seems that I managed to elongate a street somehow - In addition to the three routes I accidentally dragged while drawing the now-deleted (I believe) 335-Centro Morumbi route, looks like the nodes of the route are now counted as part of Rua Tarobá (Tarobá Street). This was a little too good, tried a few softwares to draw bus routes, lost so much time that it was much better if I had done them manually on iD from day one. I was a bit too happy when I realized that Potlach 2 could do it.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-brazil" rel="tag" title="see questions tagged &#39;brazil&#39;">brazil</span> <span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-route" rel="tag" title="see questions tagged &#39;route&#39;">route</span> <span class="post-tag tag-link-changes" rel="tag" title="see questions tagged &#39;changes&#39;">changes</span> <span class="post-tag tag-link-undo" rel="tag" title="see questions tagged &#39;undo&#39;">undo</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>20 May '16, 00:45</strong></p>
<img src="https://secure.gravatar.com/avatar/b1766e693b5356aaa12c4de8302c9eac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="thribeiro&#39;s gravatar image" />
<p><span>thribeiro</span><br />
<span class="score" title="11 reputation points">11</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="thribeiro has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 May '16, 00:55</strong> </span></p>
</div>
</div>
<div id="comments-container-49749" class="comments-container">
<span id="49752"></span>
<div id="comment-49752" class="comment">
<div id="post-49752-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I just had a short look: <a href="https://www.openstreetmap.org/relation/3586878">https://www.openstreetmap.org/relation/3586878</a> was not touched by you. Where is it "damaged"?</p>
<p>So you want a revert of #39439327 until #39413772 (see <a href="https://www.openstreetmap.org/user/thribeiro/history">https://www.openstreetmap.org/user/thribeiro/history</a> )? Could you confirm? And then just wait a bit. Someone experienced will do it for you (maybe myself in about 12 hours), that's no problem. Reverting is not possible with Potlatch after you have saved/uploaded the edit.</p>
</div>
<div id="comment-49752-info" class="comment-info">
<span class="comment-age">(20 May '16, 06:41)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49765"></span>
<div id="comment-49765" class="comment">
<div id="post-49765-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I confirm that I want my changes #39439327, #39439273, #39413948 and #39413772 undone. I hope that does the trick. Thank you for your time.</p>
<p>You can see here <a href="http://i.imgsafe.org/357de83.jpg">http://i.imgsafe.org/357de83.jpg</a> an example of what's going on now (one street counting now as three). In the meantime, I stopped entirely to avoid further problems.</p>
<p>I find it odd that I don't appear on the changeset for those. However, now on another computer (so I can confirm those aren't cache issues) I see that not only Rua/Street Tarobá is affected, but also Rua Maguari too, both of them now spanning the entire length of the bus routes I tried to add.</p>
<p>Even though I don't show up, I believe this is somehow my fault - It's no coincidence that those three routes and streets now share the exact same shape as the relation I drew before.</p>
<p>I gave up trying to use gtfs-editor (too many issues), and commercial software trials revealed to be worse than iD. We'd have to add the routes to OSM afterwards anyway.</p>
</div>
<div id="comment-49765-info" class="comment-info">
<span class="comment-age">(20 May '16, 17:40)</span> <span class="comment-user userinfo">thribeiro</span>
</div>
</div>
<span id="49766"></span>
<div id="comment-49766" class="comment">
<div id="post-49766-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>half-offtopic: If you want to map bus route relations please use <a href="https://wiki.openstreetmap.org/wiki/JOSM">JOSM</a>. Take a slow start, maybe first also map other stuff. It takes a bit to learn but really pays off! :-)</p>
<p>I will look at the revert stuff now.</p>
</div>
<div id="comment-49766-info" class="comment-info">
<span class="comment-age">(20 May '16, 21:16)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49767"></span>
<div id="comment-49767" class="comment">
<div id="post-49767-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a>: could you please comment too instead of just voting down my comment (which should not really happen UI-wise)? I am confused. In case you mean my typo ("bug" instead of "bus") - fixed.</p>
</div>
<div id="comment-49767-info" class="comment-info">
<span class="comment-age">(20 May '16, 21:25)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49769"></span>
<div id="comment-49769" class="comment">
<div id="post-49769-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, I'll check JOSM.</p>
</div>
<div id="comment-49769-info" class="comment-info">
<span class="comment-age">(20 May '16, 22:51)</span> <span class="comment-user userinfo">thribeiro</span>
</div>
</div>
<span id="49771"></span>
<div id="comment-49771" class="comment not_top_scorer">
<div id="post-49771-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/5179/aseerel4c26"></a><a href="http://help.openstreetmap.org/users/5179/aseerel4c26">@aseerel4c26</a> It simply isn't true to say that "errors wouldn't be made if users used JOSM" instead of some other editor. A quick count back through the last dozen or so issues where I've had to get involved fixing stuff (either locally or, with a DWG hat on, more widely). Here's the tally of the editors used:</p>
<pre><code>JOSM                                         6
iD                                           2
osmapi (i.e. some other front-end program):  2
Potlatch 2                                   1</code></pre>
<p>I suspect that that ratio (apart from osmapi) isn't that far away from the amount of data those editors are used for within OSM. The most time consuming of that list above were jointly a series of sock-puppet accounts making the same unwelcome changes (which happened to be JOSM, but would have been problematic regardless of editor) and a series of "delete and redraw" errors that were done by JOSM, and had an editor been used that showed relation membership more prominently may not have been made.</p>
</div>
<div id="comment-49771-info" class="comment-info">
<span class="comment-age">(21 May '16, 00:07)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="49775"></span>
<div id="comment-49775" class="comment not_top_scorer">
<div id="post-49775-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/387/someoneelse"></a><a href="http://help.openstreetmap.org/users/387/someoneelse">@SomeoneElse</a> thanks for the explanation. Please note that I did not say what you've quoted. Not at all. It is just my personal experience that JOSM gives you a clearer more data centric view, more tools to check your edits and, hence, is easier to use than Potlatch2 or iD. This is at least true for complex tasks. And I, personally, made the switch far too late (torture myself by using Potlatch2 for too long) and I want help others to be more productive and have more fun. I remember how time consuming and annoying it was to separate terraced buildings into single ones with Potlatch2.</p>
</div>
<div id="comment-49775-info" class="comment-info">
<span class="comment-age">(21 May '16, 10:13)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49749" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-49749-form-container" class="comment-form-container">
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

<span id="49768"></span>

<div id="answer-container-49768" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49768-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49768-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-49768-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I have reverted your changesets 39439327 39439273 39413948 39413772 by <a href="https://www.openstreetmap.org/changeset/39459612">https://www.openstreetmap.org/changeset/39459612</a></p>
<p>What seems to be the main cause of the issue is that you have elongated two ways (streets) by very much: Rua Tarobá and Rua Maguari. See <a href="https://overpass-api.de/achavi/?changeset=39413948">https://overpass-api.de/achavi/?changeset=39413948</a> (may take about a minute to load). The green lines are the new positions of the ways. You can position your mouse pointer over those to see the whole way highlighted and its name.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 May '16, 21:43</strong></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="aseerel4c26 has 169 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 May '16, 12:14</strong> </span></p>
</div>
</div>
<div id="comments-container-49768" class="comments-container">
&#10;</div>
<div id="comment-tools-49768" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49768-form-container" class="comment-form-container">
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

