+++
type = "question"
title = "Bus stops without name"
description = '''Seems like a simple question: How to tag bus stops without a name? highway=bus_stop tells me to tag a node next to one side of the highway way. Ok, but i prefer public_transport=stop_position with public_transport=platform. As far as I understand I need to add a key:name on both nodes or add a publi...'''
date = "2014-08-17T05:33:00Z"
lastmod = "2014-08-20T17:48:00Z"
weight = 35908
keywords = [ "bus", "public-transport", "busstops", "tagging" ]
aliases = [ "/questions/35908" ]
osqa_answers = 3
osqa_accepted = true
+++

<div class="headNormal">

# [Bus stops without name](/questions/35908/bus-stops-without-name)

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
<span id="post-35908-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35908-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-35908-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Seems like a simple question: How to tag bus stops without a name?</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Tag:highway%3Dbus_stop">highway=bus_stop</a> tells me to tag a node next to one side of the highway way. Ok, but i prefer <a href="http://wiki.openstreetmap.org/wiki/Tag:public_transport%3Dstop_position">public_transport=stop_position</a> with <a href="http://wiki.openstreetmap.org/wiki/Tag:public_transport%3Dplatform">public_transport=platform</a>. As far as I understand I need to add a <a href="http://wiki.openstreetmap.org/wiki/Key:name">key:name</a> on both nodes or add a <a href="http://wiki.openstreetmap.org/wiki/Tag:public_transport%3Dstop_area">public_transport=stop_area</a> relation. Unfortunately this also needs a <a href="http://wiki.openstreetmap.org/wiki/Key:name">key:name</a>. So what can I do?</p>
<p>I also read <a href="http://wiki.openstreetmap.org/wiki/Proposed_features/Noname">Proposed features/Noname</a> and <a href="http://wiki.openstreetmap.org/wiki/Names#No_name">Names/No_Name</a> but could not find an answer. The closest "answer" I have found is <a href="https://help.openstreetmap.org/answer_link/19204/">this</a> but I am still not sure if this is correct.</p>
<p>(Background: I am trying to add some bus stations on a bus route like <a href="http://www.openstreetmap.org/relation/3586878#map=13/-25.5733/-54.5335&amp;layers=T">this</a> in Brazil. But the bus stops seem to be unnamed and I have no idea how to "link" the platforms with stop_positions).</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-bus" rel="tag" title="see questions tagged &#39;bus&#39;">bus</span> <span class="post-tag tag-link-public-transport" rel="tag" title="see questions tagged &#39;public-transport&#39;">public-transport</span> <span class="post-tag tag-link-busstops" rel="tag" title="see questions tagged &#39;busstops&#39;">busstops</span> <span class="post-tag tag-link-tagging" rel="tag" title="see questions tagged &#39;tagging&#39;">tagging</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Aug '14, 05:33</strong></p>
<img src="https://secure.gravatar.com/avatar/490606febe7fb9d385ad826263611247?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="jkirk&#39;s gravatar image" />
<p><span>jkirk</span><br />
<span class="score" title="66 reputation points">66</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="9 badges"><span class="bronze">●</span><span class="badgecount">9</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="jkirk has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-35908" class="comments-container">
&#10;</div>
<div id="comment-tools-35908" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35908-form-container" class="comment-form-container">
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

3 Answers:

</div>

</div>

<span id="35910"></span>

<div id="answer-container-35910" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35910-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35910-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-35910-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="jkirk has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Just tag it with noname=yes. You could also add a note so other mappers know for sure there is (currently) no name. Nobody knows whether this might change in the future.</p>
<p>If the busstop has no name, you can safely ignore the "need to add" from the public transport "specification".</p>
<p>Or you could ask the locals, whether they give the busstop a name.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '14, 08:22</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-35910" class="comments-container">
<span id="35978"></span>
<div id="comment-35978" class="comment">
<div id="post-35978-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok. I could do that but that does not solve the "link-problem". How is the "stop_position"(s) linked with "platform"(s) (for the very same bus stop) if no bus stop name is given?</p>
</div>
<div id="comment-35978-info" class="comment-info">
<span class="comment-age">(19 Aug '14, 05:45)</span> <span class="comment-user userinfo">jkirk</span>
</div>
</div>
<span id="35980"></span>
<div id="comment-35980" class="comment">
<div id="post-35980-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>by adding a stop area relation: <a href="http://wiki.openstreetmap.org/wiki/Tag:public_transport%3Dstop_area">http://wiki.openstreetmap.org/wiki/Tag:public_transport%3Dstop_area</a></p>
</div>
<div id="comment-35980-info" class="comment-info">
<span class="comment-age">(19 Aug '14, 06:08)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
<span id="36028"></span>
<div id="comment-36028" class="comment">
<div id="post-36028-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you very much. I just tried(tm) adding a stop_area without a name like <a href="http://www.openstreetmap.org/relation/3975420">http://www.openstreetmap.org/relation/3975420</a> and it worked. I was thinking all the time that relations are linked with an unique name (which is not needed as the relation has a unique ID).</p>
<p>But: part of the confusion seems to come from this: <a href="http://wiki.openstreetmap.org/wiki/Bus_stop#Stop_area">http://wiki.openstreetmap.org/wiki/Bus_stop#Stop_area</a></p>
<p>There the name-tag is mandatory. Shouldn't that be corrected?</p>
</div>
<div id="comment-36028-info" class="comment-info">
<span class="comment-age">(20 Aug '14, 17:40)</span> <span class="comment-user userinfo">jkirk</span>
</div>
</div>
<span id="36029"></span>
<div id="comment-36029" class="comment">
<div id="post-36029-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>And one more thing: look at this stop_area: <a href="http://www.openstreetmap.org/relation/949291#map=18/47.08459/15.45657&amp;layers=T">http://www.openstreetmap.org/relation/949291#map=18/47.08459/15.45657&amp;layers=T</a></p>
<p>and compare it with "my" newly created one: <a href="http://www.openstreetmap.org/relation/3975420#map=18/-25.53994/-54.58729&amp;layers=T">http://www.openstreetmap.org/relation/3975420#map=18/-25.53994/-54.58729&amp;layers=T</a></p>
<p>The first stop_area is surrounded with a nice border. Why isn't that shown on the second stop_area?</p>
</div>
<div id="comment-36029-info" class="comment-info">
<span class="comment-age">(20 Aug '14, 17:45)</span> <span class="comment-user userinfo">jkirk</span>
</div>
</div>
<span id="36030"></span>
<div id="comment-36030" class="comment">
<div id="post-36030-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/9469/jkirk"></a><a href="http://help.openstreetmap.org/users/9469/jkirk">@jkirk</a> - (re the name-tag being mandatory) that's part of the problem with the "public transport v2" stuff on that page. It's simply not a good fit for public transport in most of the world, is overcomplicated, and deters people from capturing useful information. Personally, where the wiki's wrong in cases like this I just ignore it - I've largely given up arguing with the people who edit the wiki (who in some cases don't seem to do much mapping).</p>
</div>
<div id="comment-36030-info" class="comment-info">
<span class="comment-age">(20 Aug '14, 17:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-35910" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35910-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35949"></span>

<div id="answer-container-35949" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35949-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35949-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-35949-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This is a classic example of the JOSM validator creating false negatives.</p>
<p>There is no reason why a bus stop needs a name. Although in most countries in Western Europe this is typical nowadays, but it's not so long ago that bus stops only had signs. Of course bus stops had informal names, but its relatively recently that transport authorities have tried to codify naming. Elsewhere in the world I would expect standard names for bus stops not to exist. The JOSM validator is then raising incorrect errors.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>18 Aug '14, 09:54</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-35949" class="comments-container">
<span id="35979"></span>
<div id="comment-35979" class="comment">
<div id="post-35979-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yeah, but the JOSM validator is my minor problem. How is the "stop_position" linked with the "platform" without a name tag?</p>
</div>
<div id="comment-35979-info" class="comment-info">
<span class="comment-age">(19 Aug '14, 05:47)</span> <span class="comment-user userinfo">jkirk</span>
</div>
</div>
<span id="35985"></span>
<div id="comment-35985" class="comment">
<div id="post-35985-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Use official bus stop number as ref and use the ref in the relation.</p>
</div>
<div id="comment-35985-info" class="comment-info">
<span class="comment-age">(19 Aug '14, 09:58)</span> <span class="comment-user userinfo">erkinalp</span>
</div>
</div>
<span id="35989"></span>
<div id="comment-35989" class="comment">
<div id="post-35989-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>It's not just JOSM that's broken then!</p>
</div>
<div id="comment-35989-info" class="comment-info">
<span class="comment-age">(19 Aug '14, 13:25)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="36013"></span>
<div id="comment-36013" class="comment">
<div id="post-36013-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>If the bus stop is served by a bus route then just add the platform node to that bus route as well as the street the bus uses. The stop_position node is then linked because it is part of the street.</p>
<p>If the bus stop isn't served by a bus route, i.e. buses don't stop there regularly, then there is by definition anyway no stop postion and it doesn't make sense to map one.</p>
</div>
<div id="comment-36013-info" class="comment-info">
<span class="comment-age">(20 Aug '14, 07:54)</span> <span class="comment-user userinfo">Roland Olbricht</span>
</div>
</div>
</div>
<div id="comment-tools-35949" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35949-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="35920"></span>

<div id="answer-container-35920" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-35920-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-35920-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-35920-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most timetables that i have seen use landmarks such as " The Golden Lion " " The Market Square XXX" or the name of the street crossing the route which is close to the stop, isn't that the solution for the "name"?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Aug '14, 13:09</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Aug '14, 13:11</strong> </span></p>
</div>
</div>
<div id="comments-container-35920" class="comments-container">
&#10;</div>
<div id="comment-tools-35920" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-35920-form-container" class="comment-form-container">
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

