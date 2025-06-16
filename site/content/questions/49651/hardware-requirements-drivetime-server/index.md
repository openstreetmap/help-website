+++
type = "question"
title = "Hardware Requirements Drivetime Server"
description = '''We intend to set up one or more dedicated OSM servers to manage almost exclusively drive time calculations. Using an offline solution, we manage 10-15 thousand drive time requests per machine per day (at constant 99% i7-CPU). Doing spot checks on Google, it handles easily several hundred requests a ...'''
date = "2016-05-10T19:49:00Z"
lastmod = "2017-01-26T14:29:00Z"
weight = 49651
keywords = [ "drivetimes", "hardwarerequirements", "routing", "server" ]
aliases = [ "/questions/49651" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Hardware Requirements Drivetime Server](/questions/49651/hardware-requirements-drivetime-server)

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
<span id="post-49651-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49651-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-49651-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>We intend to set up one or more dedicated OSM servers to manage almost exclusively drive time calculations. Using an offline solution, we manage 10-15 thousand drive time requests per machine per day (at constant 99% i7-CPU). Doing spot checks on Google, it handles easily several hundred requests a minute. But we do not know their system architecture and they limit to 1 Mio a year either way - we do those in a few weeks today (offline, local machines). Coverage should initially be Europe and North America. Better on two different machines? How will CPU and RAM influence the speed of complex drive time calculations? I've seen the info on mapping servers, but our focus is drive time calculation, not the mapping.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-drivetimes" rel="tag" title="see questions tagged &#39;drivetimes&#39;">drivetimes</span> <span class="post-tag tag-link-hardwarerequirements" rel="tag" title="see questions tagged &#39;hardwarerequirements&#39;">hardwarerequirements</span> <span class="post-tag tag-link-routing" rel="tag" title="see questions tagged &#39;routing&#39;">routing</span> <span class="post-tag tag-link-server" rel="tag" title="see questions tagged &#39;server&#39;">server</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 May '16, 19:49</strong></p>
<img src="https://secure.gravatar.com/avatar/bc0e5374fcd1506a7c4e42018c120530?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Osm_ccom&#39;s gravatar image" />
<p><span>Osm_ccom</span><br />
<span class="score" title="25 reputation points">25</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Osm_ccom has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 May '16, 21:29</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></p>
</div>
</div>
<div id="comments-container-49651" class="comments-container">
<span id="49652"></span>
<div id="comment-49652" class="comment">
<div id="post-49652-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>I guess it will be useful if you would mention which routing algorithm/library you are using.</p>
</div>
<div id="comment-49652-info" class="comment-info">
<span class="comment-age">(10 May '16, 19:59)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49654"></span>
<div id="comment-49654" class="comment">
<div id="post-49654-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I. Have. No. Idea :-D Okay, a basic draft one: <a href="http://www.yournavigation.org/">http://www.yournavigation.org/</a> uses <a href="https://wiki.openstreetmap.org/wiki/YOURS">https://wiki.openstreetmap.org/wiki/YOURS</a> and as Routing-Engine <a href="https://wiki.openstreetmap.org/wiki/Gosmore.">https://wiki.openstreetmap.org/wiki/Gosmore.</a> We thought to try this first and then compare the results with the results from +20 engines (on- and offline, ie. Google, Bing, Apple, Maptitude, etc., etc.) we have on file (we used to "callibrate" our results) I thought if someone has experience with the hardware-requirements, there would be likely ideas what to use in such a scenario...? ツ</p>
</div>
<div id="comment-49654-info" class="comment-info">
<span class="comment-age">(10 May '16, 20:13)</span> <span class="comment-user userinfo">Osm_ccom</span>
</div>
</div>
<span id="49655"></span>
<div id="comment-49655" class="comment">
<div id="post-49655-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>"I. Have. No. Idea" is also helpful. :-) If you do not yet know this wiki page... here it is: <a href="https://wiki.openstreetmap.org/wiki/Routing">Routing</a>. From what I've read in the past is that graphhopper and osrm are at least among the fastest ones. If you are looking for isochrones: OpenRouteService has such a feature. Other people here will be able to help you more, stand by.</p>
</div>
<div id="comment-49655-info" class="comment-info">
<span class="comment-age">(10 May '16, 20:36)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="49671"></span>
<div id="comment-49671" class="comment">
<div id="post-49671-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks! I/we saw the Routing page, but this is gibberish if you simply used existing, ready software. I also looked at <a href="https://lists.openstreetmap.org/listinfo/routing">https://lists.openstreetmap.org/listinfo/routing</a> but our need is rather uncommon and there's contradictory information on solutions to use and they're all into single calculations, we talk about mass calculations. Common isochrones use simply drivetime on the minute, the "quick and dirty" solution that brings quick results but doesn't work. We need to associate statistical data, so we must go by fixed points that match given statistical administrative regions around the point of origin. That's my question. If you do MASS computations of drive times... What requirements should the server meet? What's the bottleneck? CPU, RAM? On our current tool, system runs at constant average of 99% CPU and we talk about reasonably current i7s Quad Core - of which we use effectively only two cores, adding a third or fourth only slows down the system... How is that in OSM. I do NOT know, if I'll get an answer, I do believe we pioneer something here... I just want to avoid running into an avoidable bottle neck when I buy new but the wrong hardware...</p>
</div>
<div id="comment-49671-info" class="comment-info">
<span class="comment-age">(11 May '16, 07:52)</span> <span class="comment-user userinfo">Osm_ccom</span>
</div>
</div>
</div>
<div id="comment-tools-49651" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49651-form-container" class="comment-form-container">
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

<span id="49672"></span>

<div id="answer-container-49672" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-49672-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-49672-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-49672-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p><a href="http://project-osrm.org/">OSRM</a> will give the fastest results for your purposes, using the viaroute or matrix calls.</p>
<p>In general, OSRM is limited by RAM rather than CPU. You will need at least a 64GB machine to create the routing data for North America or Europe, possibly even 128GB. However, once you are up and running, the requirements are less: North America and Western Europe will need around 10GB each.</p>
<p>You may want to consider using cloud hosting (e.g. AWS or DigitalOcean) for the preprocessing, and then commodity hardware to run the server: I use my own hardware for the former and Hetzner servers for the latter. As long as the architectures and OSs are compatible (e.g. both Ubuntu on x86), you can move the routing files from one to another.</p>
<p>OSRM has a demo public API which you can use to test whether it is suitable for your application.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>11 May '16, 08:47</strong></p>
<img src="https://secure.gravatar.com/avatar/08324717c25d6067fa4ff23ef37d455f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Richard&#39;s gravatar image" />
<p><span>Richard ♦</span><br />
<span class="score" title="30902 reputation points"><span>30.9k</span></span><span title="44 badges"><span class="badge1">●</span><span class="badgecount">44</span></span><span title="279 badges"><span class="silver">●</span><span class="badgecount">279</span></span><span title="412 badges"><span class="bronze">●</span><span class="badgecount">412</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Richard has 98 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 May '16, 09:57</strong> </span></p>
</div>
</div>
<div id="comments-container-49672" class="comments-container">
<span id="54301"></span>
<div id="comment-54301" class="comment">
<div id="post-54301-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>According to the message you used different OSRM versions. Try to use the same OSRM version as during the pre-processig step. Also please create a new question next time.</p>
</div>
<div id="comment-54301-info" class="comment-info">
<span class="comment-age">(26 Jan '17, 13:43)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="54303"></span>
<div id="comment-54303" class="comment">
<div id="post-54303-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> your comment makes more sense agains the next answer</p>
</div>
<div id="comment-54303-info" class="comment-info">
<span class="comment-age">(26 Jan '17, 14:00)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="54304"></span>
<div id="comment-54304" class="comment">
<div id="post-54304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The "next answer" is actually a comment on this one :) It can't be moved because of a bug in OSQA (because it's been edited I think).</p>
</div>
<div id="comment-54304-info" class="comment-info">
<span class="comment-age">(26 Jan '17, 14:09)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="54305"></span>
<div id="comment-54305" class="comment">
<div id="post-54305-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Yes. I commented subbuj9's answer and then tried to move his "answer" to this answer. Due to the OSQA bug the answer can't be moved but the comment has been moved nevertheless :(</p>
</div>
<div id="comment-54305-info" class="comment-info">
<span class="comment-age">(26 Jan '17, 14:12)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="54308"></span>
<div id="comment-54308" class="comment">
<div id="post-54308-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/158/scai">@scai</a> (as you've discovered now) you need to do that the other way around for it to work :)</p>
</div>
<div id="comment-54308-info" class="comment-info">
<span class="comment-age">(26 Jan '17, 14:25)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-49672" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-49672-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="54300"></span>

<div id="answer-container-54300" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-54300-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-54300-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-54300-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi Richard,</p>
<p>I used Azure cloud (Ubuntu 14, north america continental) for the pre-processing and successfully done. Moved files to local Ubuntu server. Getting below warning when i run the osrm-routed. Please help.</p>
<p>[warn] .hsgr was prepared with different build. Reprocess to get rid of this warning.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>26 Jan '17, 13:07</strong></p>
<img src="https://secure.gravatar.com/avatar/9cf1b8a88a3889d53b3673cf1794f385?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="subbuj9&#39;s gravatar image" />
<p><span>subbuj9</span><br />
<span class="score" title="1 reputation points">1</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="subbuj9 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>26 Jan '17, 13:08</strong> </span></p>
</div>
</div>
<div id="comments-container-54300" class="comments-container">
<span id="54309"></span>
<div id="comment-54309" class="comment">
<div id="post-54309-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ignoring the warning, do the requests actually work?</p>
</div>
<div id="comment-54309-info" class="comment-info">
<span class="comment-age">(26 Jan '17, 14:29)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-54300" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-54300-form-container" class="comment-form-container">
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

