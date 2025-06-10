+++
type = "question"
title = "How to correct location of an address pointer on the map?"
description = '''I&#x27;m new to using Openstreetmap.org. I like the idea that users can correct and improve the data, much like Wikipedia, but documentation for doing basic editing tasks seems very hard to find. I&#x27;ve searched in various locations on the openstreetmap.org site, including this question database.  When I s...'''
date = "2013-07-17T14:13:00Z"
lastmod = "2013-07-18T19:29:00Z"
weight = 24307
keywords = [ "correction", "addresses", "correcting", "pointers", "address" ]
aliases = [ "/questions/24307" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [How to correct location of an address pointer on the map?](/questions/24307/how-to-correct-location-of-an-address-pointer-on-the-map)

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
<span id="post-24307-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24307-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-24307-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I'm new to using Openstreetmap.org. I like the idea that users can correct and improve the data, much like Wikipedia, but documentation for doing basic editing tasks seems very hard to find. I've searched in various locations on the openstreetmap.org site, including this question database.</p>
<p>When I search for my business address "3720 Canton St, Dallas, TX" Two conflicting locations are returned, one wrong by about a block, and the other is near our building but the pointer is maybe 50 feet away in the middle of a street. Here's the permalink to the area in question:</p>
<p><a href="http://www.openstreetmap.org/?lat=32.785349&amp;lon=-96.773407&amp;zoom=18&amp;layers=M">http://www.openstreetmap.org/?lat=32.785349&amp;lon=-96.773407&amp;zoom=18&amp;layers=M</a></p>
<p>I tried selecting "edit" and various editor options but in each case the address pointer vanishes when the editor loads, so there's nothing I can find to move or edit with regard to the address. One of the two pointers needs to be deleted completely, the other should be moved, presumably to the entrance of the building. I'd like to make the edits myself so that I can learn how and correct other entries as well, if someone can point me to the documentation on how to do it. What I would find helpful is a simple, step-by-step guide for new users with how-tos for basic tasks (e.g. "how to correct an address pointer", "how to remove a non-existent street", "how to correct a street name", etc.) Or if something like that already exists maybe its location could communicated to new users more effectively - including in the sign-up email or displayed on the sign-up page?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-correction" rel="tag" title="see questions tagged &#39;correction&#39;">correction</span> <span class="post-tag tag-link-addresses" rel="tag" title="see questions tagged &#39;addresses&#39;">addresses</span> <span class="post-tag tag-link-correcting" rel="tag" title="see questions tagged &#39;correcting&#39;">correcting</span> <span class="post-tag tag-link-pointers" rel="tag" title="see questions tagged &#39;pointers&#39;">pointers</span> <span class="post-tag tag-link-address" rel="tag" title="see questions tagged &#39;address&#39;">address</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>17 Jul '13, 14:13</strong></p>
<img src="https://secure.gravatar.com/avatar/d5b711fb29b5fa42331cb06941514e50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steevithak&#39;s gravatar image" />
<p><span>Steevithak</span><br />
<span class="score" title="226 reputation points">226</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steevithak has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-24307" class="comments-container">
&#10;</div>
<div id="comment-tools-24307" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24307-form-container" class="comment-form-container">
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

<span id="24308"></span>

<div id="answer-container-24308" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24308-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24308-score" class="post-score" title="current number of votes">
6
</div>
<span id="post-24308-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>The reason that you can not find anything to edit is because the house in not actually in the OpenStreetMap data set. This has been found in an external (non-osm) data set called 'tiger' which isn't very acurate. If you add house numbers in this area in OSM this will be used in preference so simply adding the property in the correct location should fix things.</p>
<p>There was already an answer to the question on <a href="https://help.openstreetmap.org/questions/7335/how-to-add-a-house-number">how to add house numbers</a> that you may find provides the information you are after.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '13, 14:30</strong></p>
<img src="https://secure.gravatar.com/avatar/bda08a105bb6a4a606d47c1b27187fac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="twain&#39;s gravatar image" />
<p><span>twain</span><br />
<span class="score" title="2381 reputation points"><span>2.4k</span></span><span title="25 badges"><span class="silver">●</span><span class="badgecount">25</span></span><span title="38 badges"><span class="bronze">●</span><span class="badgecount">38</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="twain has 15 accepted answers">40%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jul '13, 14:31</strong> </span></p>
</div>
</div>
<div id="comments-container-24308" class="comments-container">
<span id="24314"></span>
<div id="comment-24314" class="comment">
<div id="post-24314-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Partial success - I added the building and assigned an address. Ran into a few minor issues: 1) there doesn't seem to be an easy way to constrain the polygon to a rectangle, so it may not be accurate. 2) the map still refers to the location as a "house" - how do I tell the database that this is a business? 3) this building has multiple tenants, how do I specify the suite numbers and business names?</p>
</div>
<div id="comment-24314-info" class="comment-info">
<span class="comment-age">(17 Jul '13, 16:24)</span> <span class="comment-user userinfo">Steevithak</span>
</div>
</div>
<span id="24320"></span>
<div id="comment-24320" class="comment">
<div id="post-24320-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Looks like you've got it figured out and nominatum now finds you if you search for "ncc internet services" as well as the street address.</p>
</div>
<div id="comment-24320-info" class="comment-info">
<span class="comment-age">(17 Jul '13, 17:41)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="24327"></span>
<div id="comment-24327" class="comment">
<div id="post-24327-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes, I'm slowly getting there. One thing that still puzzles me. Even though I've now added the building and business name, nothing shows up on the map when browsing that area. It does show up if I do a search for the specific address but if I just browse to that area of the map, the building outline is not visible. Other buildings in nearby areas are visible, so it appears I'm still doing something wrong. I've written the step-by-step of what I did in my own answer below - am I leaving out a step that is needed to make the building outline visible on the map?</p>
</div>
<div id="comment-24327-info" class="comment-info">
<span class="comment-age">(17 Jul '13, 19:51)</span> <span class="comment-user userinfo">Steevithak</span>
</div>
</div>
<span id="24328"></span>
<div id="comment-24328" class="comment">
<div id="post-24328-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>That just sounds like the usual "the map hasn't quite updated yet" issue. There are lots of previous answers on that topic - search for <a href="https://help.openstreetmap.org/search/?Submit=Search&amp;t=question">visible</a> for a list. It's not that long ago that the main map only updated once a week...</p>
</div>
<div id="comment-24328-info" class="comment-info">
<span class="comment-age">(17 Jul '13, 23:06)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="24336"></span>
<div id="comment-24336" class="comment">
<div id="post-24336-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, it's there for me now. I suspect you got a bit unlucky with the time of your edit coinciding with a data replication delay <a href="http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/replication_delay.html">http://munin.openstreetmap.org/openstreetmap/yevaud.openstreetmap/replication_delay.html</a> so time to render would have been longer than is (now) usual.</p>
</div>
<div id="comment-24336-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 08:27)</span> <span class="comment-user userinfo">EdLoach ♦</span>
</div>
</div>
</div>
<div id="comment-tools-24308" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24308-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24318"></span>

<div id="answer-container-24318" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24318-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24318-score" class="post-score" title="current number of votes">
4
</div>
<span id="post-24318-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hate to answer my own question because I'm definitely no expert on this but here's what I've figured out so far:</p>
<ol>
<li>Click the Edit drop-down menu and select "Edit with iD"</li>
<li>Click the "area" menu</li>
<li>Draw a box that outlines the satellite image of the building</li>
<li>Click the house icon in the center of the new area</li>
<li>Select the second icon (clockwise) to square up the corners if needed</li>
<li>On the "Select Feature Type" dialog that appears on the right, pick "Building"</li>
<li>Fill in the building data including the address (see caveat below)</li>
<li>Click Save</li>
</ol>
<p>Once the correct address is assimilated by the system, it apparently drops any duplicate address pointers.</p>
<p>Caveats: The system doesn't appear to be able to handle multi-use or multi-tenant buildings, so there's no way to add business names, websites, addresses with suite numbers, etc. for that type of building. A work-around seems to be creating "points" of type "other" to represent each suite and adding the business names and other data to those.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '13, 16:56</strong></p>
<img src="https://secure.gravatar.com/avatar/d5b711fb29b5fa42331cb06941514e50?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Steevithak&#39;s gravatar image" />
<p><span>Steevithak</span><br />
<span class="score" title="226 reputation points">226</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="silver">●</span><span class="badgecount">4</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Steevithak has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Jul '13, 23:24</strong> </span></p>
</div>
</div>
<div id="comments-container-24318" class="comments-container">
<span id="24346"></span>
<div id="comment-24346" class="comment">
<div id="post-24346-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A very thorough answer. You can potentially add suite numbers by adding addr:suite=lower-upper, and addr:interpolation=all, but this will only work if suites are numbered consecutively, otherwise add all suite numbers (for instance if they are based on floor numbers) addr:suite=suite1;suite3;suite5 ... This still doesn't solve the multiple occupant problem, but at least would represent the set of valid addresses.</p>
</div>
<div id="comment-24346-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 12:27)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="24360"></span>
<div id="comment-24360" class="comment">
<div id="post-24360-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks, I've seen several references to doing things by "adding X=Y" type stuff but all such explanations leave out any mention of HOW you add X=Y. Is there documentation somewhere on that? The editors themselves don't have any obvious button or control that suggests it would allow you type in arbitrary text of that sort.</p>
</div>
<div id="comment-24360-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 16:17)</span> <span class="comment-user userinfo">Steevithak</span>
</div>
</div>
<span id="24361"></span>
<div id="comment-24361" class="comment">
<div id="post-24361-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>In Potlatch 2, there are always "simple" and "advanced" views available when you've clicked on something and are displaying details of it. After adding a new thing initially you'll see in simple mode "no tags set"; if you click "advanced" and then "add" you can add whatever tags you like.</p>
</div>
<div id="comment-24361-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 17:59)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="24363"></span>
<div id="comment-24363" class="comment">
<div id="post-24363-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>At the bottom of the right pane of the iD-editor there is a section "All tags". You might need to scroll down to see it and you probably have to click on it to expand it. Once it is visible, you can click on the big "+" at the bottom to add any tag you want.</p>
</div>
<div id="comment-24363-info" class="comment-info">
<span class="comment-age">(18 Jul '13, 19:29)</span> <span class="comment-user userinfo">cartinus</span>
</div>
</div>
</div>
<div id="comment-tools-24318" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24318-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24310"></span>

<div id="answer-container-24310" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24310-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24310-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-24310-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Your business isn't currently in the database, and the search engine (nominatim) is estimating based on the road (and as the road is in sections, the two results you mention are near the midpoint of a couple of the sections that make up Canton Street).</p>
<p>Adding the building and it's address should mean future searches will pinpoint your business accurately.</p>
<p>I notice from your earlier changeset that you are using Potlatch 2 to edit. The new iD editor does include a short tutorial for new users. (Aside: I noticed your changeset comment "Changes may be confirmed by view sat images, comparing to Google maps, or checking in person." - just a reminder that the Bing imagery you can see in the editor is OK for use, as is the checking in person, but we can't use Google's maps due to copyright (<a href="http://www.deadlinenews.co.uk/2013/07/05/google-says-sorry-for-sinking-island/">and they might be wrong</a>.)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '13, 14:35</strong></p>
<img src="https://secure.gravatar.com/avatar/f25a8392e12ed696b16554b3d08e4e2b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EdLoach&#39;s gravatar image" />
<p><span>EdLoach ♦</span><br />
<span class="score" title="19478 reputation points"><span>19.5k</span></span><span title="16 badges"><span class="badge1">●</span><span class="badgecount">16</span></span><span title="156 badges"><span class="silver">●</span><span class="badgecount">156</span></span><span title="280 badges"><span class="bronze">●</span><span class="badgecount">280</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EdLoach has 93 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-24310" class="comments-container">
<span id="24316"></span>
<div id="comment-24316" class="comment">
<div id="post-24316-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wasn't advocating that someone should copy data from a Google map. I assumed there is some sort of moderation process through which my edit would go before becoming public and that the those moderators might want a way of verifying that my changes were legitimate, so I offered several ways they could be validated.</p>
</div>
<div id="comment-24316-info" class="comment-info">
<span class="comment-age">(17 Jul '13, 16:42)</span> <span class="comment-user userinfo">Steevithak</span>
</div>
</div>
</div>
<div id="comment-tools-24310" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24310-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="24313"></span>

<div id="answer-container-24313" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-24313-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-24313-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-24313-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Also, when you add your building you can tag with your business name, phone number, web site, etc.</p>
<p>I don't think the phone number and web site are used for much at the moment, but nominatim will also find things by name so searches for your business name will return your address and location.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Jul '13, 15:51</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-24313" class="comments-container">
<span id="24317"></span>
<div id="comment-24317" class="comment">
<div id="post-24317-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Unfortunately, this is a mixed use building with multiple residential and business tenants, each with their own suite number. The database appears to assume that each building has only one tenant, so it's unclear how to enter the business names and websites. Otherwise, I'd be happy to do so.</p>
</div>
<div id="comment-24317-info" class="comment-info">
<span class="comment-age">(17 Jul '13, 16:45)</span> <span class="comment-user userinfo">Steevithak</span>
</div>
</div>
<span id="24319"></span>
<div id="comment-24319" class="comment">
<div id="post-24319-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Buildings can be "terraced", that is subdivided and then the individual businesses tagged to each part.</p>
<p>Or you can just add a node for each business, approximately where they are located in the building and tag the information on that.</p>
<p>Not sure how this can be done with iD as I switched from Potlatch to JOSM a while back and never looked at iD.</p>
</div>
<div id="comment-24319-info" class="comment-info">
<span class="comment-age">(17 Jul '13, 17:36)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-24313" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-24313-form-container" class="comment-form-container">
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

