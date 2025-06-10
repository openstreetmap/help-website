+++
type = "question"
title = "is cyclability a derivative data? need to make available?"
description = '''I&#x27;ve just started using OSM and am making a commercial cycle map for an NGO. It will cover Denpasar city in Indonesia, which doesn&#x27;t yet have anything similar. The aim is to inform people on how to commute without needing to use main roads (as opposed to sports cycling). I plan to use OSM data, but ...'''
date = "2018-01-15T06:44:00Z"
lastmod = "2018-01-17T11:15:00Z"
weight = 61634
keywords = [ "available", "derivative", "use", "license", "cycle" ]
aliases = [ "/questions/61634" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [is cyclability a derivative data? need to make available?](/questions/61634/is-cyclability-a-derivative-data-need-to-make-available)

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
<span id="post-61634-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61634-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-61634-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I've just started using OSM and am making a commercial cycle map for an NGO. It will cover Denpasar city in Indonesia, which doesn't yet have anything similar. The aim is to inform people on how to commute without needing to use main roads (as opposed to sports cycling).</p>
<p>I plan to use OSM data, but adding in an attribute column for 'suitability for cycling', for categorizing the display symbols. No data except mine and OSM's will be used. The distinction is fairly arbitrary: as there don't exist any designated cycle paths in Denpasar, I'm simply basing my distinctions on how subjectively safe and pleasant it feels to use these roads, and whether they are useful throughroads.</p>
<p><strong>My question is this</strong>: do I need to make the data on cyclability available for other users? If so, how should I do this?</p>
<p>I don't see that this data is particularly useful to anyone, as the lack of standardized classifications means that they won't really mean anything except to cyclists who've used the map. Neither can I reclassify the roads as 'cycleways' or change the accessibility classification; as bicycles are <em>allowed</em> to cycle on most roads, even if not <em>advised</em> to do so. Furthermore, there are few cyclable roads which exclude cars or motorbikes.</p>
<p>If it is something that I ought to upload, please tell me how I should do that. Thanks! Sorry if this is a stupid question!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-available" rel="tag" title="see questions tagged &#39;available&#39;">available</span> <span class="post-tag tag-link-derivative" rel="tag" title="see questions tagged &#39;derivative&#39;">derivative</span> <span class="post-tag tag-link-use" rel="tag" title="see questions tagged &#39;use&#39;">use</span> <span class="post-tag tag-link-license" rel="tag" title="see questions tagged &#39;license&#39;">license</span> <span class="post-tag tag-link-cycle" rel="tag" title="see questions tagged &#39;cycle&#39;">cycle</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>15 Jan '18, 06:44</strong></p>
<img src="https://secure.gravatar.com/avatar/3d0cd8219bcdca4ba0d07d7878a1ce11?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Plattypus&#39;s gravatar image" />
<p><span>Plattypus</span><br />
<span class="score" title="81 reputation points">81</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Plattypus has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-61634" class="comments-container">
&#10;</div>
<div id="comment-tools-61634" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61634-form-container" class="comment-form-container">
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

<span id="61653"></span>

<div id="answer-container-61653" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61653-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61653-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-61653-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There have been questions like this in the past. "Cyclability" seems rather subjective, which makes it a bad tag.</p>
<p>I think it is much better to map objective criteria such as road width, the existence of cycle lane / track, number of lanes, max speed , road surface, smoothness, etc. You can then take all those parameters into account to calculate a "cyclability"-number for your app.</p>
<p>Take a look at cycle.travel, they use pure OSM-data to create the best cycle route. (In some countries they do use traffic information from other sources, as well as elevation information).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jan '18, 06:05</strong></p>
<img src="https://secure.gravatar.com/avatar/813a136afe7d4c95fd5bccdd78705e0e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="escada&#39;s gravatar image" />
<p><span>escada</span><br />
<span class="score" title="19043 reputation points"><span>19.0k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="166 badges"><span class="silver">●</span><span class="badgecount">166</span></span><span title="302 badges"><span class="bronze">●</span><span class="badgecount">302</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="escada has 97 accepted answers">21%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>16 Jan '18, 06:05</strong> </span></p>
</div>
</div>
<div id="comments-container-61653" class="comments-container">
<span id="61671"></span>
<div id="comment-61671" class="comment">
<div id="post-61671-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply, escada. I've had a look at cycle.travel, and like the idea. I don't think I'd be able to get hold of the data you mentioned, unfortunately. I haven't found many roads in my area on OSM that have those tags either, so will probably follow Andy Allan's suggestion and upload the data as a separate link.</p>
</div>
<div id="comment-61671-info" class="comment-info">
<span class="comment-age">(17 Jan '18, 02:13)</span> <span class="comment-user userinfo">Plattypus</span>
</div>
</div>
</div>
<div id="comment-tools-61653" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61653-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61656"></span>

<div id="answer-container-61656" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61656-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61656-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-61656-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems to me like you are proposing to create a database derived from OpenStreetMap data. You talk about adding a "column" or attribute to existing OSM data. So in my opinion (and I'm not a lawyer etc), this would be classified as a derived database, and not a collective database. See <a href="https://wiki.osmfoundation.org/wiki/Licence/Community_Guidelines/Collective_Database_Guideline_Guideline">these community guidelines</a> for more information.</p>
<p>Since you're making a derived database, then there are some share-alike requirements. There is a good explanation <a href="https://wiki.osmfoundation.org/wiki/Licence/Licence_and_Legal_FAQ#What_do_you_mean_by_Share-Alike.3F">on share-alike requirements</a> in the Licence FAQ. But to answer your question, you need to provide the data when asked. You don't need to upload the data to OpenStreetMap, but putting a link to download your data somewhere on your own website would be nice.</p>
<p>In your particular case, you are quite right to build your own database containing this subjective information, instead of editing OSM directly.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>16 Jan '18, 10:05</strong></p>
<img src="https://secure.gravatar.com/avatar/c3743b1b368f5e209eb8aad30164acc4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Andy%20Allan&#39;s gravatar image" />
<p><span>Andy Allan</span><br />
<span class="score" title="12456 reputation points"><span>12.5k</span></span><span title="23 badges"><span class="badge1">●</span><span class="badgecount">23</span></span><span title="128 badges"><span class="silver">●</span><span class="badgecount">128</span></span><span title="153 badges"><span class="bronze">●</span><span class="badgecount">153</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Andy Allan has 46 accepted answers">28%</span></p>
</div>
</div>
<div id="comments-container-61656" class="comments-container">
<span id="61672"></span>
<div id="comment-61672" class="comment">
<div id="post-61672-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply, Andy Allan. I think I'll do that, then - upload the data separately and provide a link.</p>
</div>
<div id="comment-61672-info" class="comment-info">
<span class="comment-age">(17 Jan '18, 02:16)</span> <span class="comment-user userinfo">Plattypus</span>
</div>
</div>
</div>
<div id="comment-tools-61656" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61656-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="61638"></span>

<div id="answer-container-61638" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-61638-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-61638-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-61638-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The data you want to add seems to be worthy of adding to OSM itself, and having your data in OSM simplifies a lot of steps.</p>
<p>Have a look at the <a href="https://wiki.openstreetmap.org/wiki/Key:class:bicycle">class:bicycle</a> tag, which looks pretty much like what you describe. See also the general <a href="https://wiki.openstreetmap.org/wiki/Bicycle">bicycle</a> page for more tags that relate to cycling even if only indirectly (like <a href="https://wiki.openstreetmap.org/wiki/Key:smoothness">smoothness</a> or <a href="https://wiki.openstreetmap.org/wiki/Maxspeed">maxspeed</a>).</p>
<p>Last but not least, have a look at the <a href="https://www.cyclestreets.net/">cyclestreets</a> project, which has a router geared towards cycling that takes into account many osm tags. You should be able to setup a cyclestreets instance for your area, check what OSM tags they use, and maybe even tweak the heuristics to take your own tags into account.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>15 Jan '18, 11:26</strong></p>
<img src="https://secure.gravatar.com/avatar/d20f86db9a6f03cb070e9fbaaf0b7228?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vincent%20de%20Phily&#39;s gravatar image" />
<p><span>Vincent de P... ♦</span><br />
<span class="score" title="17304 reputation points"><span>17.3k</span></span><span title="18 badges"><span class="badge1">●</span><span class="badgecount">18</span></span><span title="152 badges"><span class="silver">●</span><span class="badgecount">152</span></span><span title="249 badges"><span class="bronze">●</span><span class="badgecount">249</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Vincent de Phily has 64 accepted answers">19%</span></p>
</div>
</div>
<div id="comments-container-61638" class="comments-container">
<span id="61648"></span>
<div id="comment-61648" class="comment">
<div id="post-61648-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>They specifically state that their new data is subjective and arbitrary, which means it shouldn't be included in the public OSM database.</p>
</div>
<div id="comment-61648-info" class="comment-info">
<span class="comment-age">(15 Jan '18, 19:10)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
<span id="61673"></span>
<div id="comment-61673" class="comment">
<div id="post-61673-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for your reply, Vincent de Philly. I like the idea of the router, however my area doesn't have many roads with the tags you mention. For the class:bicycle tag, I'm afraid it seems a little too complicated for my brain to handle at the moment, so I'll follow Andy Allan's suggestion to upload my data separately. Maybe later when I've gotten my head around it and tested the roads more times I'll come back and assign them bicycle:commuter values, as they do seem more useful.</p>
</div>
<div id="comment-61673-info" class="comment-info">
<span class="comment-age">(17 Jan '18, 02:28)</span> <span class="comment-user userinfo">Plattypus</span>
</div>
</div>
<span id="61680"></span>
<div id="comment-61680" class="comment">
<div id="post-61680-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>ĨMHO the class:bicycle tag fits the OP's usecase well. While restricting ourselves to 100% objective tags is a worthy goal, it can never be reached, and in practice we already have a lot of subjective tags in OSM, particularly about road classifications.</p>
</div>
<div id="comment-61680-info" class="comment-info">
<span class="comment-age">(17 Jan '18, 10:34)</span> <span class="comment-user userinfo">Vincent de P... ♦</span>
</div>
</div>
<span id="61682"></span>
<div id="comment-61682" class="comment">
<div id="post-61682-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>A group like <a href="http://www.fietsersbond.be/">Fietsersbond.be</a> (Site in Dutch) tries to measure the quality of the cycling infrastructure with AFAIK mainly objective criteria (width, surface, etc.) Maybe because that is the only argument that holds against politicians ?</p>
</div>
<div id="comment-61682-info" class="comment-info">
<span class="comment-age">(17 Jan '18, 11:15)</span> <span class="comment-user userinfo">escada</span>
</div>
</div>
</div>
<div id="comment-tools-61638" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-61638-form-container" class="comment-form-container">
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

