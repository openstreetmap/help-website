+++
type = "question"
title = "How to implement a Mapnik sandbox without installing anything?"
description = '''Last couple of weeks I spent some time building fake counties, cities and suburbs in Nevada desert (where I figured it would not hurt anyone) just to see how they would render in Mapnik. (I am working on a problem of getting county, city and name rendered without having to drop a place=* node where ...'''
date = "2011-04-18T19:12:00Z"
lastmod = "2011-04-20T23:51:00Z"
weight = 4605
keywords = [ "qa", "sandbox", "testing", "mapnik" ]
aliases = [ "/questions/4605" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How to implement a Mapnik sandbox without installing anything?](/questions/4605/how-to-implement-a-mapnik-sandbox-without-installing-anything)

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
<span id="post-4605-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4605-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-4605-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Last couple of weeks I spent some time building fake counties, cities and suburbs in Nevada desert (where I figured it would not hurt anyone) just to see how they would render in Mapnik. (I am working on a problem of getting county, city and name rendered without having to drop a place=* node where I want to see the label and I have not found the solution yet, but that's a separate question.)</p>
<p>It occurred to me that I many not be going the best way about it:<br />
- I needlessly load the server with rerender requests<br />
- I have to wait a fairly long time for rerenders, so I am limited in how many tagging scenario I can try<br />
- even though I delete my objects afterwards, it is possible that Nominatim (or other indexers) will have time to pick them; and I don't think Nominatim is very good at deleting its objects in response to OSM deletions.</p>
<p>Is there a safe way to play with OSM/Mapnik without installing any server components of my own? Is there an official Mapnik sandbox perhaps, and if not, how can I create one on the fly?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-qa" rel="tag" title="see questions tagged &#39;qa&#39;">qa</span> <span class="post-tag tag-link-sandbox" rel="tag" title="see questions tagged &#39;sandbox&#39;">sandbox</span> <span class="post-tag tag-link-testing" rel="tag" title="see questions tagged &#39;testing&#39;">testing</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>18 Apr '11, 19:12</strong></p>
<img src="https://secure.gravatar.com/avatar/c23c2891306229bb036de7ce63bb8c9b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ponzu&#39;s gravatar image" />
<p><span>ponzu</span><br />
<span class="score" title="2104 reputation points"><span>2.1k</span></span><span title="49 badges"><span class="badge1">●</span><span class="badgecount">49</span></span><span title="64 badges"><span class="silver">●</span><span class="badgecount">64</span></span><span title="83 badges"><span class="bronze">●</span><span class="badgecount">83</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ponzu has no accepted answers">0%</span> </br></br></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Nov '13, 21:33</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/66f0dc05b44574e3894be07b0b37cf37?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="aseerel4c26&#39;s gravatar image" />
<p><span>aseerel4c26 ♦</span><br />
<span class="score" title="32615 reputation points"><span>32.6k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="248 badges"><span class="silver">●</span><span class="badgecount">248</span></span><span title="554 badges"><span class="bronze">●</span><span class="badgecount">554</span></span></br></p>
</div>
</div>
<div id="comments-container-4605" class="comments-container">
<span id="4685"></span>
<div id="comment-4685" class="comment">
<div id="post-4685-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Is there nothing else online to try rendering test objects in the context of the real OSM data? So far, having a Nevada test site is the best I can do. My only concern is potential impact on Nominatim. I am not clear on how long I can leave my fake cities, counties and other objects in the desert without risk of having them become part of the index.</p>
</div>
<div id="comment-4685-info" class="comment-info">
<span class="comment-age">(20 Apr '11, 22:56)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-4605" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4605-form-container" class="comment-form-container">
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

<span id="4610"></span>

<div id="answer-container-4610" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4610-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4610-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4610-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For producing your own tiles without installing big software frameworks have a look at</p>
<p><a href="https://wiki.openstreetmap.org/wiki/Maps_on_a_Stick">Maps_on_a_Stick</a> or <a href="https://wiki.openstreetmap.org/wiki/OpenStreetMap-in-a-Box">OpenStreetMap-in-a-Box</a></p>
<p>When you have detailed questions about one of this or other solutions, come over to the <a href="http://forum.osm.org">OSM forum</a> or the <a href="https://wiki.openstreetmap.org/wiki/Mailing_lists">OSM mailinglists</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Apr '11, 20:36</strong></p>
<img src="https://secure.gravatar.com/avatar/245b73d4390c3408fe3c6da759b9897f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="stephan75&#39;s gravatar image" />
<p><span>stephan75</span><br />
<span class="score" title="12642 reputation points"><span>12.6k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="56 badges"><span class="silver">●</span><span class="badgecount">56</span></span><span title="210 badges"><span class="bronze">●</span><span class="badgecount">210</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="stephan75 has 37 accepted answers">6%</span></p>
</div>
</div>
<div id="comments-container-4610" class="comments-container">
<span id="4619"></span>
<div id="comment-4619" class="comment">
<div id="post-4619-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, looks like one or both can fit the bill, although Maps On a Stick have a 219 Mb download. As far as osminabox, would "how do I get started?" be considered a detailed question?</p>
</div>
<div id="comment-4619-info" class="comment-info">
<span class="comment-age">(18 Apr '11, 22:39)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4620"></span>
<div id="comment-4620" class="comment">
<div id="post-4620-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>And the second question before I forget: the tiles I produce with these service would be Mapnik tiles, right? And if so, will they be using the master OSM stylesheet, a stylesheet that's specific to these services, or a stylesheet of my choosing?</p>
</div>
<div id="comment-4620-info" class="comment-info">
<span class="comment-age">(18 Apr '11, 22:40)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-4610" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4610-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4688"></span>

<div id="answer-container-4688" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4688-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4688-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-4688-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Adding things to OSM which don't actually exist is vandalism. Please don't do it.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>20 Apr '11, 23:11</strong></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vclaw has 41 accepted answers">22%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>20 Apr '11, 23:11</strong> </span></p>
</div>
</div>
<div id="comments-container-4688" class="comments-container">
<span id="4689"></span>
<div id="comment-4689" class="comment">
<div id="post-4689-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Understood. Do you have anything you can recommend as an officially approved rendering sandbox? I am a fairly technical guy (not that I understand how OSM or Mapnik works), but I could not figure out how get started with stephan's advice above.</p>
</div>
<div id="comment-4689-info" class="comment-info">
<span class="comment-age">(20 Apr '11, 23:15)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="4690"></span>
<div id="comment-4690" class="comment">
<div id="post-4690-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>There is a dev API, which you can add things to without bothering anyone: <a href="http://api06.dev.openstreetmap.org">http://api06.dev.openstreetmap.org</a> Though I'm not sure if it will actually be rendered by anything.</p>
</div>
<div id="comment-4690-info" class="comment-info">
<span class="comment-age">(20 Apr '11, 23:22)</span> <span class="comment-user userinfo">Vclaw</span>
</div>
</div>
<span id="4692"></span>
<div id="comment-4692" class="comment">
<div id="post-4692-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, it looks promising, but I need to figure out a way to get my changes rendered. Is that (easily) doable? After all, I was looking for a Mapnik sandbox, not OSM sandbox. (Although it's good to know where it is in case I need it one day.)</p>
</div>
<div id="comment-4692-info" class="comment-info">
<span class="comment-age">(20 Apr '11, 23:51)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
</div>
<div id="comment-tools-4688" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4688-form-container" class="comment-form-container">
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

