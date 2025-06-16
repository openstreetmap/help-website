+++
type = "question"
title = "How do I disable the mousewheel zoom feature?"
description = '''Google Maps v3 has an option ---&amp;gt; scrollwheel=&quot;false&quot; Is something like this available for OpenStreetMap?'''
date = "2012-12-28T21:15:00Z"
lastmod = "2021-11-23T15:33:00Z"
weight = 18746
keywords = [ "scrollwheel", "mousewheel", "zoom", "disable" ]
aliases = [ "/questions/18746" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How do I disable the mousewheel zoom feature?](/questions/18746/how-do-i-disable-the-mousewheel-zoom-feature)

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
<span id="post-18746-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18746-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-18746-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Google Maps v3 has an option ---&gt; scrollwheel="false"</p>
<p>Is something like this available for OpenStreetMap?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-scrollwheel" rel="tag" title="see questions tagged &#39;scrollwheel&#39;">scrollwheel</span> <span class="post-tag tag-link-mousewheel" rel="tag" title="see questions tagged &#39;mousewheel&#39;">mousewheel</span> <span class="post-tag tag-link-zoom" rel="tag" title="see questions tagged &#39;zoom&#39;">zoom</span> <span class="post-tag tag-link-disable" rel="tag" title="see questions tagged &#39;disable&#39;">disable</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>28 Dec '12, 21:15</strong></p>
<img src="https://secure.gravatar.com/avatar/64b5f1cb59bb94fd6c2661393666291a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Nu%20Everest&#39;s gravatar image" />
<p><span>Nu Everest</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Nu Everest has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-18746" class="comments-container">
<span id="18747"></span>
<div id="comment-18747" class="comment">
<div id="post-18747-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>OpenStreetMap is, at its core, just a <a href="http://planet.osm.org/">large lump of data</a>. <a href="https://wiki.openstreetmap.org/wiki/Maps">Many different options</a> are available for getting this data in front of a user. So the answer is "yes, if you want there to be".</p>
<p>Or perhaps you could explain a little bit more about what you're trying to do?<br />
</p>
<p>I'm guessing that it involves <a href="http://switch2osm.org/serving-tiles/">a web-based map of some sort, possibly made up of map tiles</a>, but could you be more specific?</p>
</div>
<div id="comment-18747-info" class="comment-info">
<span class="comment-age">(28 Dec '12, 21:31)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="18748"></span>
<div id="comment-18748" class="comment">
<div id="post-18748-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Yeah I'm guessing you're actually asking about OpenLayers or Leaflet. You need to state this in your question</p>
</div>
<div id="comment-18748-info" class="comment-info">
<span class="comment-age">(29 Dec '12, 02:17)</span> <span class="comment-user userinfo">Harry Wood</span>
</div>
</div>
<span id="18750"></span>
<div id="comment-18750" class="comment">
<div id="post-18750-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>You could I guess use Google Maps to display OpenStreetMap tiles as per this example: <a href="https://wiki.openstreetmap.org/wiki/Google_Maps_Example">https://wiki.openstreetmap.org/wiki/Google_Maps_Example</a></p>
</div>
<div id="comment-18750-info" class="comment-info">
<span class="comment-age">(29 Dec '12, 11:34)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
<span id="18755"></span>
<div id="comment-18755" class="comment not_top_scorer">
<div id="post-18755-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I just want to make my page in a way that the user can scroll down the page and over the map without getting sucked into the map.</p>
<p>I am aware that OpenLayers provides such a feature i.e. <a href="http://www.stoimen.com/blog/2009/06/20/openlayers-disable-mouse-wheel-on-zoom/">http://www.stoimen.com/blog/2009/06/20/openlayers-disable-mouse-wheel-on-zoom/</a></p>
<p>However, to get access to what seems like a simple feature I have to include a massive OpenLayers JS file that gives me the ability to do a bunch of cool things that I don't need.</p>
<p>I was hoping that I could simply define a setting in the Embeddable HTML.</p>
<p>It seems like the answer is, no.</p>
</div>
<div id="comment-18755-info" class="comment-info">
<span class="comment-age">(29 Dec '12, 17:33)</span> <span class="comment-user userinfo">Nu Everest</span>
</div>
</div>
<span id="28613"></span>
<div id="comment-28613" class="comment not_top_scorer">
<div id="post-28613-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm trying to remove embed Google Map on my customers websites, but as Nu Everest, I'm lookign for an easy way to disable the scroll (zoom) when the mouse is hover the map. Many customers have bad come back with this fonctionnality (specially when the embed map is big and when the visitor just want to scroll down the website page).</p>
<p>So I think it could be very usefull for OSM growing to implement a scrollwheelzoom="false" option on the embed code.</p>
</div>
<div id="comment-28613-info" class="comment-info">
<span class="comment-age">(30 Nov '13, 12:20)</span> <span class="comment-user userinfo">Spheerys</span>
</div>
</div>
<span id="28614"></span>
<div id="comment-28614" class="comment">
<div id="post-28614-score" class="comment-score">
2
</div>
<div class="comment-text">
<p><span></span><span>@Spheerys</span> As already described in the other answers/comments this has nothing to do with OpenStreetMap but instead is a Leaflet/OpenLayers/whateveryouareusing-issue.</p>
</div>
<div id="comment-28614-info" class="comment-info">
<span class="comment-age">(30 Nov '13, 14:14)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="39861"></span>
<div id="comment-39861" class="comment not_top_scorer">
<div id="post-39861-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, wondering if this is still not possible in OSM?</p>
<p>I have put a very simple embed (literally just showing where something is on the map) on a website -- but on scroll it obviously goes a little crazy with zooming. So, I would like to disable mousewheel zoom.</p>
</div>
<div id="comment-39861-info" class="comment-info">
<span class="comment-age">(28 Dec '14, 01:14)</span> <span class="comment-user userinfo">popovichN</span>
</div>
</div>
<span id="39862"></span>
<div id="comment-39862" class="comment">
<div id="post-39862-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/10228/popovichn">@popovichN</a>: it IS possible. See the comments above.</p>
</div>
<div id="comment-39862-info" class="comment-info">
<span class="comment-age">(28 Dec '14, 02:37)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-18746" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-18746-form-container" class="comment-form-container">
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

<span id="18757"></span>

<div id="answer-container-18757" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-18757-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-18757-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-18757-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Leaflet is small, easy to use and does include mousewheel support. It is worth looking at.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Dec '12, 19:01</strong></p>
<img src="https://secure.gravatar.com/avatar/b906204accce0fd58bc408b22bae01f2?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="ChrisH&#39;s gravatar image" />
<p><span>ChrisH</span><br />
<span class="score" title="4075 reputation points"><span>4.1k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="42 badges"><span class="silver">●</span><span class="badgecount">42</span></span><span title="62 badges"><span class="bronze">●</span><span class="badgecount">62</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="ChrisH has 11 accepted answers">15%</span> </br></p>
</div>
</div>
<div id="comments-container-18757" class="comments-container">
<span id="18761"></span>
<div id="comment-18761" class="comment">
<div id="post-18761-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you for all of your responses. Leaflet looks like a great answer thanks!</p>
</div>
<div id="comment-18761-info" class="comment-info">
<span class="comment-age">(29 Dec '12, 22:35)</span> <span class="comment-user userinfo">Nu Everest</span>
</div>
</div>
</div>
<div id="comment-tools-18757" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-18757-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="82659"></span>

<div id="answer-container-82659" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-82659-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-82659-score" class="post-score" title="current number of votes">
-3
</div>
<span id="post-82659-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Please be clear:</p>
<p>Can you avoid scrolling in a web map insert with the options provided by the openstreetmap GUI? NO, YOU CAN'T.</p>
<p>If there is a method, please give a useful answer. If you are concerned about the use of openstreetmap on the web, please suggest such an improvement.</p>
<p>Thanks</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>23 Nov '21, 13:51</strong></p>
<img src="https://secure.gravatar.com/avatar/236a38953ec302356f175c04e758394a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Screatius&#39;s gravatar image" />
<p><span>Screatius</span><br />
<span class="score" title="-2 reputation points">-2</span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Screatius has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-82659" class="comments-container">
<span id="82662"></span>
<div id="comment-82662" class="comment">
<div id="post-82662-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Some how I doubt that commenting on a 9 year old answer is going to achieve anything.</p>
</div>
<div id="comment-82662-info" class="comment-info">
<span class="comment-age">(23 Nov '21, 15:33)</span> <span class="comment-user userinfo">SimonPoole ♦</span>
</div>
</div>
</div>
<div id="comment-tools-82659" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-82659-form-container" class="comment-form-container">
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

