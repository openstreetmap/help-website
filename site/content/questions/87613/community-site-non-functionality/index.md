+++
type = "question"
title = "community site non-functionality"
description = '''This site [help.openstreetmap.org] keeps suggesting to visit community.openstreetmap.org as well. When I try to look at that, &quot;discourse&quot; only keeps griping about my browser [which is recent and there&#x27;s little or nothing wrong with it] and I can&#x27;t see any way to either search or log in over there. I...'''
date = "2023-08-06T14:14:00Z"
lastmod = "2023-08-07T11:56:00Z"
weight = 87613
keywords = [ "discourse", "javascript", "community", "browser" ]
aliases = [ "/questions/87613" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [community site non-functionality](/questions/87613/community-site-non-functionality)

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
<span id="post-87613-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87613-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-87613-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>This site [help.openstreetmap.org] keeps suggesting to visit community.openstreetmap.org as well. When I try to look at that, "discourse" only keeps griping about my browser [which is recent and there's little or nothing wrong with it] and I can't see any way to either search or log in over there. In the browser error console, it throws some garbage like</p>
<blockquote>
<p><em>Uncaught Unsupported browser detected start-discourse-f6e4e67026eabe0c9b84599087eb11ee33d8149f196b7439b0630ed5ab4d5f29.js:10:5 &lt;anonymous&gt; <a href="https://community-cdn.openstreetmap.org/brotli_asset/start-discourse-f6e4e67026eabe0c9b84599087eb11ee33d8149f196b7439b0630ed5ab4d5f29.js:10">https://community-cdn.openstreetmap.org/brotli_asset/start-discourse-f6e4e67026eabe0c9b84599087eb11ee33d8149f196b7439b0630ed5ab4d5f29.js:10</a> &lt;anonymous&gt; <a href="https://community-cdn.openstreetmap.org/brotli_asset/start-discourse-f6e4e67026eabe0c9b84599087eb11ee33d8149f196b7439b0630ed5ab4d5f29.js:22">https://community-cdn.openstreetmap.org/brotli_asset/start-discourse-f6e4e67026eabe0c9b84599087eb11ee33d8149f196b7439b0630ed5ab4d5f29.js:22</a></em></p>
</blockquote>
<p>which should not be a show-stopping error. Jeez, c'mon. Generic Firefox on Linux, figure it out already.</p>
<p>So, two questions:</p>
<p>What is the RIGHT place to ask questions these days? Here or "community" ?</p>
<p>Why did OSM pick such a crippled platform to base "community" around, where it's evidently so picky about exact user-agent headers that it refuses to gracefully fall back to a working configuration and deliver basic functionality?</p>
<p>_H*</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-discourse" rel="tag" title="see questions tagged &#39;discourse&#39;">discourse</span> <span class="post-tag tag-link-javascript" rel="tag" title="see questions tagged &#39;javascript&#39;">javascript</span> <span class="post-tag tag-link-community" rel="tag" title="see questions tagged &#39;community&#39;">community</span> <span class="post-tag tag-link-browser" rel="tag" title="see questions tagged &#39;browser&#39;">browser</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>06 Aug '23, 14:14</strong></p>
<img src="https://secure.gravatar.com/avatar/3031665c506b04f416a1af103cf8cf6e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="_Hobbit&#39;s gravatar image" />
<p><span>_Hobbit</span><br />
<span class="score" title="51 reputation points">51</span><span title="6 badges"><span class="badge1">●</span><span class="badgecount">6</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="_Hobbit has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-87613" class="comments-container">
<span id="87616"></span>
<div id="comment-87616" class="comment">
<div id="post-87616-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>What version of Firefox is it?</p>
</div>
<div id="comment-87616-info" class="comment-info">
<span class="comment-age">(06 Aug '23, 15:44)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87624"></span>
<div id="comment-87624" class="comment">
<div id="post-87624-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>FF 91 ESR, fairly recent which works with everything else I throw it at and should be supported for a long time to come. My useragent header may be slightly different from stock, but that should <em>never</em> matter to a correctly designed site.</p>
<p>Did Discourse do something screwy with javascript like what broke iD a while back? Or are they being deliberately obstructionist?</p>
</div>
<div id="comment-87624-info" class="comment-info">
<span class="comment-age">(06 Aug '23, 21:15)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
<span id="87625"></span>
<div id="comment-87625" class="comment not_top_scorer">
<div id="post-87625-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Do other Discourse sites such as <a href="https://meta.discourse.org/">https://meta.discourse.org/</a> work? If not, it sounds like something you'd want to report upstream.</p>
</div>
<div id="comment-87625-info" class="comment-info">
<span class="comment-age">(06 Aug '23, 21:47)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87630"></span>
<div id="comment-87630" class="comment not_top_scorer">
<div id="post-87630-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Same results, but then I changed my useragent to fake "firefox 99" and then it looked more normal. That's pretty short-sighted on their part, but I'll try to poke their support if they even have any.</p>
<p>I can't understand why OSM is even suggesting that people use that mess, let alone migrate to that if that's the intent of the red message bar at the top of this help site. What's wrong with this mechanism right here? There are WAY too many different places to attempt to get help with OSM, it's confusing AF, and adding yet another one just makes things worse.</p>
</div>
<div id="comment-87630-info" class="comment-info">
<span class="comment-age">(06 Aug '23, 23:24)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
<span id="87632"></span>
<div id="comment-87632" class="comment">
<div id="post-87632-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Given what I've seen I'd frankly rather <em>not</em> use Discourse, because this help forum seems to have been perfectly adequate for a long time and there's no reason to move to a broken platform because someone thinks it's all new and shiny. C'mon, people. Think bigger please. By splitting a help forum into two or three different and mutually exclusive pieces, you're losing audience and confusing those who have no idea all these different things exist.</p>
<p>[I say "two or three" because it's not just this and Discourse, I had to go all the way to Github to get my last problem actually noticed and fixed. Super-frustrating.]</p>
</div>
<div id="comment-87632-info" class="comment-info">
<span class="comment-age">(07 Aug '23, 00:39)</span> <span class="comment-user userinfo">_Hobbit</span>
</div>
</div>
<span id="87634"></span>
<div id="comment-87634" class="comment">
<div id="post-87634-score" class="comment-score">
1
</div>
<div class="comment-text">
<blockquote>
<p>Given what I've seen I'd frankly rather not use Discourse</p>
</blockquote>
<p>That's OK; it's not compulsory! That said, OSQA (which is the software that this forum uses) is unsupported and has to be dragged kicking and screaming onto new platforms as OSM upgrades servers. The long-term plan is for c.osm.org to replace this site, but it's not at feature parity yet.</p>
</div>
<div id="comment-87634-info" class="comment-info">
<span class="comment-age">(07 Aug '23, 01:04)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="87638"></span>
<div id="comment-87638" class="comment">
<div id="post-87638-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>FYI Firefox 91 ESR has been unsupported for nearly a year (<a href="https://endoflife.date/firefox">source</a>).</p>
<p>On debian "oldstable" (with security updates) I get FF 102 ESR, which works with Discourse.</p>
</div>
<div id="comment-87638-info" class="comment-info">
<span class="comment-age">(07 Aug '23, 11:56)</span> <span class="comment-user userinfo">H_mlet</span>
</div>
</div>
</div>
<div id="comment-tools-87613" class="comment-tools">
<span class="comments-showing"> showing 5 of 7 </span> <a href="#" class="show-all-comments-link">show 2 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-87613-form-container" class="comment-form-container">
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

<span id="87631"></span>

<div id="answer-container-87631" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-87631-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-87631-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-87631-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Quoting from <a href="https://meta.discourse.org/t/about-support-for-legacy-browsers/210258/5">here</a> - "(Discourse's) official browser support policy is the latest version of Firefox, Chrome, Safari and Edge".</p>
<p>You would therefore appear to be out of luck. If you want to use Discourse, I would suggest that you either (a) upgrade or (b) persuade Discourse (not OSM) to change that policy.</p>
<p>** FWIW I'm also running "generic Firefox on Linux" and this Browser says it's currently 115.0.2.</p>
<p>** OSM has taken the entirely sensible approach to not change the Discourse implementation at c.osm.org from the standard where it can be avoided.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Aug '23, 23:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>06 Aug '23, 23:50</strong> </span></p>
</div>
</div>
<div id="comments-container-87631" class="comments-container">
&#10;</div>
<div id="comment-tools-87631" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-87631-form-container" class="comment-form-container">
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

