+++
type = "question"
title = "how the routing OSRM algorithm works?"
description = '''Hello, I&#x27;m trying to get how OSRM routing algorithm works.  I downloaded the Project-OSRM-Web-0.1.11 and I understood the client implementation of the query, but I also got the server implementation(I downloaded Project-OSRM-Develop). Compiling Project-OSRM-Web-0.1.11 in NetBeans(html compilator) I ...'''
date = "2014-01-28T09:27:00Z"
lastmod = "2014-01-29T11:09:00Z"
weight = 30272
keywords = [ "osrm", "routing", "algorithm", "server" ]
aliases = [ "/questions/30272" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [how the routing OSRM algorithm works?](/questions/30272/how-the-routing-osrm-algorithm-works)

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
<span id="post-30272-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30272-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-30272-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello, I'm trying to get how OSRM routing algorithm works.</p>
<p>I downloaded the Project-OSRM-Web-0.1.11 and I understood the client implementation of the query, but I also got the server implementation(I downloaded Project-OSRM-Develop). Compiling Project-OSRM-Web-0.1.11 in NetBeans(html compilator) I have the same result as <a href="http://map.project-osrm.org/">http://map.project-osrm.org/</a> ; writing start/end I do a query to the server, that automatically gives me a response.</p>
<p>Now I'd like to see and understand better the server implementation, using my own files in Project-OSRM-Develop, and, if possible, I'd like to change something in the routing algorithms(I have my own way to weight nodes and archways). Thank you everybody</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-osrm" rel="tag" title="see questions tagged &#39;osrm&#39;">osrm</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-algorithm" rel="tag" title="see questions tagged &#39;algorithm&#39;">algorithm</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Jan '14, 09:27</strong></p>
<img src="https://secure.gravatar.com/avatar/3be508f311801a447f51a4dab36a0e57?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Zoifil&#39;s gravatar image" />
<p><span>Zoifil</span><br />
<span class="score" title="41 reputation points">41</span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="8 badges"><span class="silver">●</span><span class="badgecount">8</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Zoifil has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>28 Jan '14, 13:45</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-30272" class="comments-container">
<span id="30274"></span>
<div id="comment-30274" class="comment">
<div id="post-30274-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I think it would be more useful to ask the OSRM community themself: See section "support" at <a href="http://project-osrm.org/">http://project-osrm.org/</a></p>
</div>
<div id="comment-30274-info" class="comment-info">
<span class="comment-age">(28 Jan '14, 13:49)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30272" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30272-form-container" class="comment-form-container">
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

<span id="30276"></span>

<div id="answer-container-30276" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-30276-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-30276-score" class="post-score" title="current number of votes">
9
</div>
<span id="post-30276-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The algorithm itself is an implementation of <a href="http://en.wikipedia.org/wiki/Contraction_hierarchies">Contraction Hierarchies</a>.</p>
<p>However, if you want to change the weighting, you don't need to worry about the core routing algorithm. Instead, you need to change OSRM's "routing profile". This is a short program that takes the OpenStreetMap tags for a way (such as highway=primary, maxspeed=50) and returns the estimated speed that can be achieved on that way. From that, OSRM can work out the fastest routes.</p>
<p>The routing profiles are designed to be changed by those deploying OSRM, so you won't find this difficult. In your Project-OSRM directory, you'll find them in the 'profiles' directory. You'll see there are three already there: bicycle.lua, car.lua and foot.lua.</p>
<p>They're written in Lua, a simple, fast embedded scripting language that shouldn't be too alien if you have experience with other well-known scripting languages (Perl, PHP, Ruby, Python). Have a look at the differences between the three to see how you can adjust the weighting based on tags.</p>
<p>Once you've adjusted the routing profile, you simply specify it in your calls to osrm-extract and osrm-prepare. I would strongly recommend you start with a small extract (which might take 15 minutes to process), rather than a whole country or indeed the planet. Rerun it at full scale once you're happy with the results!</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>28 Jan '14, 14:32</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-30276" class="comments-container">
<span id="30292"></span>
<div id="comment-30292" class="comment">
<div id="post-30292-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you, but how I can associate the Project-OSRM-Develop with the PRoject-OSRM-Web? I'm sorry but i had never work with a server/client application and I don't know what I have to do.</p>
</div>
<div id="comment-30292-info" class="comment-info">
<span class="comment-age">(29 Jan '14, 10:09)</span> <span class="comment-user userinfo">Zoifil</span>
</div>
</div>
<span id="30296"></span>
<div id="comment-30296" class="comment">
<div id="post-30296-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Project-OSRM itself is the main code that does the routing. You will need this on your own (Unix-based) server in order to do any routing with your own weightings.</p>
<p>Project-OSRM-Web is one possible front end. It's a set of JavaScript and HTML files that provide a browser-based route-planning interface. If you were to use it, you would download the files and host them on a webserver (such as Apache) like any other web content, making sure that you point it to your Project-OSRM instance. But you can also develop your own front-end.</p>
</div>
<div id="comment-30296-info" class="comment-info">
<span class="comment-age">(29 Jan '14, 11:09)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-30276" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-30276-form-container" class="comment-form-container">
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

