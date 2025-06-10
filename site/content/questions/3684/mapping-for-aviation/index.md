+++
type = "question"
title = "mapping for aviation"
description = '''Hi guys, recently I&#x27;ve searched some information about using OSM datas for aviation. I saw that there are already nice tags for airports like parkings, apron and runways but nothing for the navigation like VORs, AEROWAYS, FIXES and REPORT POINTS (that are compulsory for make a flight plan). It would...'''
date = "2011-03-10T16:25:00Z"
lastmod = "2011-06-07T20:50:00Z"
weight = 3684
keywords = [ "aviation" ]
aliases = [ "/questions/3684" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [mapping for aviation](/questions/3684/mapping-for-aviation)

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
<span id="post-3684-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3684-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-3684-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
1
</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys, recently I've searched some information about using OSM datas for aviation. I saw that there are already nice tags for airports like parkings, apron and runways but nothing for the navigation like VORs, AEROWAYS, FIXES and REPORT POINTS (that are compulsory for make a flight plan). It would be nice using OSM data for flight planning... Thanks,</p>
<p>Abramo Fratus</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-aviation" rel="tag" title="see questions tagged &#39;aviation&#39;">aviation</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>10 Mar '11, 16:25</strong></p>
<img src="https://secure.gravatar.com/avatar/a8e1f195a4032562872414dc0a778b15?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Abramo&#39;s gravatar image" />
<p><span>Abramo</span><br />
<span class="score" title="61 reputation points">61</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Abramo has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-3684" class="comments-container">
&#10;</div>
<div id="comment-tools-3684" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3684-form-container" class="comment-form-container">
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

4 Answers:

</div>

</div>

<span id="3703"></span>

<div id="answer-container-3703" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3703-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3703-score" class="post-score" title="current number of votes">
5
</div>
<span id="post-3703-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Most information relevant to instrument flight - reporting points, fixes, airspace, as well as arrival and departure patterns - are defined without reference to the ground. A reporting point might be overhead some visible landmark but it will still be officially recorded at being at position so-and-so, rathern than "whereever that landmark is".</p>
<p>This means that most of this is not visible on the ground and thus should not be in OSM. At the same time, because that kind of information is completely independent of what's on the ground, so it is easy to keep air navigation data in a separate database and just display it on top of OSM when rendering.</p>
<p>It is possible to use software written for OSM to operate and edit a completely separate database which is probably what you should be looking at. You would only have to install the <a href="http://wiki.openstreetmap.org/wiki/Rails_port">Rails port</a> and then you can hammer away at it with your favourite OSM editor, possibly creating special presets and rendering rules for that editor. Later you would set up a rendering engine to render tiles from your database, and display them on top of OSM base tiles.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '11, 17:18</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-3703" class="comments-container">
<span id="3706"></span>
<div id="comment-3706" class="comment">
<div id="post-3706-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Oh, ok. I just asked that because I saw the beatiful project OpenSeaMap, that show you everything you need for sea navigation. IMHO I think that it can be the same for something like OpenAviationMap.</p>
<p>In instrumental flight fixes, airspace and points are extremely linked to the ground and they were created for keep a safe flight, without the collision with natural or artificial obstacles, noise reduction and so on.</p>
<p>The Rails port would be nice for me, thanks, but I was searching something that would help also other users.</p>
</div>
<div id="comment-3706-info" class="comment-info">
<span class="comment-age">(10 Mar '11, 18:49)</span> <span class="comment-user userinfo">Abramo</span>
</div>
</div>
<span id="3717"></span>
<div id="comment-3717" class="comment">
<div id="post-3717-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>The idea with the Rails port is that someone in the aviation community sets it up to capture aviation data, and it is then avaialable for everyone else to contribute to. - As far as I am aware, OpenSeaMap is mostly drawn from actual observable objects, like buoys. If OpenSeaMap were to add un-observable marine navigation data to OSM they would be told to use their own database too (with the exception of national boundaries, which are generally considered acceptable to OSM because of their high importance even though not always observable).</p>
</div>
<div id="comment-3717-info" class="comment-info">
<span class="comment-age">(11 Mar '11, 09:33)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="3718"></span>
<div id="comment-3718" class="comment">
<div id="post-3718-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>BTW, I don't think you would encounter resistance if you were to add a tag like "aviation:reporting_point=Bravo" to an existing object in OpenStreetMap, e.g. a church or bridge, and then creating a map rendering that highlights these objects, provided that the information you enter is free from copyright. But people would probably object if you placed these as objects of their own.</p>
</div>
<div id="comment-3718-info" class="comment-info">
<span class="comment-age">(11 Mar '11, 09:36)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
</div>
<div id="comment-tools-3703" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3703-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="3685"></span>

<div id="answer-container-3685" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-3685-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-3685-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-3685-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll have to forgive us, but there may not be as many aviation experts involved in OpenStreetMap as we would like.</p>
<p>Are the features you talk about physical features on the landscape, or are they just points in space that are designated as important to aviation in some way? If the former, we can probably map them, but if they're not observable in some way, they almost certainly don't belong in OpenStreetMap.</p>
<p>Also, bear in mind that any data added to OpenStreetMap can be edited (or vandalised) at any time, so it may not be suitable for use in such a safety-critical application as aviation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Mar '11, 16:43</strong></p>
<img src="https://secure.gravatar.com/avatar/9fe361843971cf8b23dc93517f00b996?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jonathan%20Bennett&#39;s gravatar image" />
<p><span>Jonathan Ben...</span><br />
<span class="score" title="8261 reputation points"><span>8.3k</span></span><span title="17 badges"><span class="badge1">●</span><span class="badgecount">17</span></span><span title="85 badges"><span class="silver">●</span><span class="badgecount">85</span></span><span title="108 badges"><span class="bronze">●</span><span class="badgecount">108</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jonathan Bennett has 21 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-3685" class="comments-container">
<span id="3688"></span>
<div id="comment-3688" class="comment">
<div id="post-3688-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>VORs, Fixes and Report Points are often visible as physical structures containing the relevant beacons, however, without aeronautical navigation equipment, their apparent function may not be obvious to the observer.</p>
</div>
<div id="comment-3688-info" class="comment-info">
<span class="comment-age">(10 Mar '11, 16:52)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
<span id="3704"></span>
<div id="comment-3704" class="comment">
<div id="post-3704-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Report points in the VFR (Visual Flight Rules) are phisical entities in the space like mountains, towers, lakes, the end of a river, that are easly recognizable and where you are obbligated to report to the Air Traffic Control you position. Flight Plans in VFR are just a list of this points.</p>
</div>
<div id="comment-3704-info" class="comment-info">
<span class="comment-age">(10 Mar '11, 17:21)</span> <span class="comment-user userinfo">Abramo</span>
</div>
</div>
<span id="3708"></span>
<div id="comment-3708" class="comment">
<div id="post-3708-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>(Rhetorical questions) So how can I verify that a VFR reporting point actually is a reporting point by visiting it in the landscape, plagiarizing absolutely no copyright protected sources at all? And how can I tell when a reporting point stops being a reporting point by just visiting it?</p>
<p>Example 1: Reporting point KARLO west of ESSV is located in the Baltic Sea, 4 Nm from the coast. Just plain water...</p>
<p>Example 2: Reporting point Älvestad at the border of ESSL CTR was a church that later on burned, but the reporting point still exists.</p>
</div>
<div id="comment-3708-info" class="comment-info">
<span class="comment-age">(10 Mar '11, 19:36)</span> <span class="comment-user userinfo">gnurk</span>
</div>
</div>
<span id="3709"></span>
<div id="comment-3709" class="comment">
<div id="post-3709-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Well, (retorical question ;D) , how can I verify a boundary by visiting it in the landscape? but you see that boundaries are mapped... See OpenSeaMap... it would be nice something like that for the aviation.</p>
</div>
<div id="comment-3709-info" class="comment-info">
<span class="comment-age">(10 Mar '11, 21:23)</span> <span class="comment-user userinfo">Abramo</span>
</div>
</div>
</div>
<div id="comment-tools-3685" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-3685-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5570"></span>

<div id="answer-container-5570" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5570-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5570-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-5570-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've mapped all the UK VORs (as far as I'm aware of) from Bing and site visits. Unfortunately, I'm not a pilot myself, so don't know their frequencies.</p>
<p><a href="http://wiki.openstreetmap.org/wiki/Tag:aeroway%3Dnavigationaid">http://wiki.openstreetmap.org/wiki/Tag:aeroway%3Dnavigationaid</a></p>
<p>Hope this helps some, Chris</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>06 Jun '11, 08:16</strong></p>
<img src="https://secure.gravatar.com/avatar/7a81832ca1b48080d1a57be29dff3a8c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="c2r&#39;s gravatar image" />
<p><span>c2r</span><br />
<span class="score" title="413 reputation points">413</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="6 badges"><span class="silver">●</span><span class="badgecount">6</span></span><span title="11 badges"><span class="bronze">●</span><span class="badgecount">11</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="c2r has 2 accepted answers">18%</span></p>
</div>
</div>
<div id="comments-container-5570" class="comments-container">
&#10;</div>
<div id="comment-tools-5570" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5570-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="4629"></span>

<div id="answer-container-4629" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4629-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4629-score" class="post-score" title="current number of votes">
-1
</div>
<span id="post-4629-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The remark about boundary is very accurate ..... I am also interested in the mapping for aviation ..... Reporting points are very interesting, but also air spaces, that clearly have no connexions with the ground for their boundaries : there is already a proposed feature for that in osm. Join the discussion ? I will have a look to trails as indicated.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>19 Apr '11, 06:12</strong></p>
<img src="https://secure.gravatar.com/avatar/25c69eb689be39eba3b200a043549b94?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="courdi95&#39;s gravatar image" />
<p><span>courdi95</span><br />
<span class="score" title="29 reputation points">29</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="courdi95 has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-4629" class="comments-container">
<span id="4656"></span>
<div id="comment-4656" class="comment">
<div id="post-4656-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>You may want to consider converting your statement to a comment (rather than answer) to avoid negative votes.</p>
</div>
<div id="comment-4656-info" class="comment-info">
<span class="comment-age">(19 Apr '11, 20:13)</span> <span class="comment-user userinfo">ponzu</span>
</div>
</div>
<span id="5602"></span>
<div id="comment-5602" class="comment">
<div id="post-5602-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>AFAIK you can't comment when you have Zero points.. But you have to participate to get rating Catch 22..</p>
</div>
<div id="comment-5602-info" class="comment-info">
<span class="comment-age">(07 Jun '11, 13:54)</span> <span class="comment-user userinfo">emj</span>
</div>
</div>
<span id="5622"></span>
<div id="comment-5622" class="comment">
<div id="post-5622-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not quite; could be enlightening to just sit back and listen before you're qualified to comment.</p>
</div>
<div id="comment-5622-info" class="comment-info">
<span class="comment-age">(07 Jun '11, 20:50)</span> <span class="comment-user userinfo">Baloo Uriza</span>
</div>
</div>
</div>
<div id="comment-tools-4629" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4629-form-container" class="comment-form-container">
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

