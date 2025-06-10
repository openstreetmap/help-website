+++
type = "question"
title = "How to see bridges using mkgmap"
description = '''hello, I&#x27;m building a map using josm, and use mkgmap to converted it for my garmin 60csx. But as I live in Africa, I need to see bridges, fuel stations and telecom antennas at low zoom.. They are very good points to understand were we are. On Tracks4africa maps, bridges are represented as POI and no...'''
date = "2011-09-21T14:10:00Z"
lastmod = "2011-09-21T23:01:00Z"
weight = 8064
keywords = [ "mkgmap", "bridge" ]
aliases = [ "/questions/8064" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to see bridges using mkgmap](/questions/8064/how-to-see-bridges-using-mkgmap)

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
<span id="post-8064-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8064-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-8064-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>hello,</p>
<p>I'm building a map using josm, and use mkgmap to converted it for my garmin 60csx.</p>
<p>But as I live in Africa, I need to see bridges, fuel stations and telecom antennas at low zoom.. They are very good points to understand were we are.</p>
<p>On Tracks4africa maps, bridges are represented as POI and not as segment.. It works well. Maybe it is possible to convert all "bridges lines" into points using mkgmap? Or maybe there is a way using styles and TYP to see them better ? I'm particularly interested to see bridges on tracks sections ! To see if we can cross the river !</p>
<p>Thanks for your help and sorry for my English.. I don't practice a lot..</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mkgmap" rel="tag" title="see questions tagged &#39;mkgmap&#39;">mkgmap</span> <span class="post-tag tag-link-bridge" rel="tag" title="see questions tagged &#39;bridge&#39;">bridge</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>21 Sep '11, 14:10</strong></p>
<img src="https://secure.gravatar.com/avatar/3e6d868fd890902785b2fc4cd31d49f7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="iero&#39;s gravatar image" />
<p><span>iero</span><br />
<span class="score" title="20 reputation points">20</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="iero has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Sep '11, 14:13</strong> </span></p>
</div>
</div>
<div id="comments-container-8064" class="comments-container">
&#10;</div>
<div id="comment-tools-8064" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8064-form-container" class="comment-form-container">
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

<span id="8067"></span>

<div id="answer-container-8067" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8067-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>A quick-and-dirty solution is to make bridges display as something else. If you're not creating routable maps, then an entry such as:</p>
<p>bridge=yes [0x29 resolution 17]</p>
<p>near the top of the "lines" file would work. "0x29" is Garmin-ese for a power line, and it displays as a nice obvious narrow line.</p>
<p>If you are creating routable maps this might break routing though (since you can't normally drive along power lines!) so maybe another code would make more sense - maybe "0x01" (used for motorways) if there are few motorways where you're creating a map? The best thing to do is to experiment and see, I suspect.<br />
</p>
<p>Make sure that your "bridge=yes" is near the top of the lines file, otherwise some other tag's representation may be used instead.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '11, 16:02</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span> </br></p>
</div>
</div>
<div id="comments-container-8067" class="comments-container">
<span id="8069"></span>
<div id="comment-8069" class="comment">
<div id="post-8069-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thanks for your answer, I'll try that, it's a good idea !</p>
<p>There are no motorway at all in the country. Biggest roads can be considered as "primary", so i'll try with motorway section, and maybe change related TYP section</p>
<p>I'll keep you informed about the result !</p>
</div>
<div id="comment-8069-info" class="comment-info">
<span class="comment-age">(21 Sep '11, 16:12)</span> <span class="comment-user userinfo">iero</span>
</div>
</div>
<span id="8073"></span>
<div id="comment-8073" class="comment">
<div id="post-8073-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Actually - one thing that I forgot about - if you're relying on bicycle routing, maybe "motorway" isn't the best choice, so I'd definitely experiment with different settings.</p>
</div>
<div id="comment-8073-info" class="comment-info">
<span class="comment-age">(21 Sep '11, 22:33)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="8075"></span>
<div id="comment-8075" class="comment">
<div id="post-8075-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It works, thanks</p>
</div>
<div id="comment-8075-info" class="comment-info">
<span class="comment-age">(21 Sep '11, 23:00)</span> <span class="comment-user userinfo">iero</span>
</div>
</div>
</div>
<div id="comment-tools-8067" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8067-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="8070"></span>

<div id="answer-container-8070" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-8070-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-8070-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-8070-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You can use something like this</p>
<p>(bridge=yes | bridge=true | bridge=viaduct) [0x2b resolution 24 continue with_actions]</p>
<p>(tunnel=yes | tunnel=true | tunnel=1) [0x2a resolution 24 continue with_actions]</p>
<p>You need to put it before the highway rules. I recommend to use a typ file to make 0x2b visible, see for an example <a href="http://www.cferrero.net/maps/guide_to_TYPs.html">http://www.cferrero.net/maps/guide_to_TYPs.html</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>21 Sep '11, 17:34</strong></p>
<img src="https://secure.gravatar.com/avatar/0f5ffc3756c4662b9dfad80b7665ac6c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ligfietser&#39;s gravatar image" />
<p><span>ligfietser</span><br />
<span class="score" title="2894 reputation points"><span>2.9k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="27 badges"><span class="silver">●</span><span class="badgecount">27</span></span><span title="57 badges"><span class="bronze">●</span><span class="badgecount">57</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ligfietser has 8 accepted answers">11%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>21 Sep '11, 17:35</strong> </span></p>
</div>
</div>
<div id="comments-container-8070" class="comments-container">
<span id="8076"></span>
<div id="comment-8076" class="comment">
<div id="post-8076-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'll try, but I need to add a TYP file, and for the moment, I try to understand styles.. Thanks for the answer, I learned the "continue with_actions" that I didn't know.</p>
</div>
<div id="comment-8076-info" class="comment-info">
<span class="comment-age">(21 Sep '11, 23:01)</span> <span class="comment-user userinfo">iero</span>
</div>
</div>
</div>
<div id="comment-tools-8070" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-8070-form-container" class="comment-form-container">
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

