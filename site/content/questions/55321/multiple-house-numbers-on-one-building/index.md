+++
type = "question"
title = "Multiple house numbers on one building"
description = '''Is there an established way of tagging house numbers on buildings which have more than one number (typically one for each entrance/staircase), without going into micro-mapping the actual positions of the entrances? Here, somebody put a range in addr:housenumber. Do routers in general understand this...'''
date = "2017-03-29T08:06:00Z"
lastmod = "2017-03-30T12:33:00Z"
weight = 55321
keywords = [ "housenumbers" ]
aliases = [ "/questions/55321" ]
osqa_answers = 4
osqa_accepted = false
+++

<div class="headNormal">

# [Multiple house numbers on one building](/questions/55321/multiple-house-numbers-on-one-building)

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
<span id="post-55321-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55321-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-55321-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Is there an established way of tagging house numbers on buildings which have more than one number (typically one for each entrance/staircase), without going into micro-mapping the actual positions of the entrances?</p>
<p><a href="http://www.openstreetmap.org/way/345070158">Here</a>, somebody put a range in addr:housenumber. Do routers in general understand this (mapnik apparently renders it). Do semicolons work (addr:housenumber=91;93;95)?</p>
<p><a href="http://www.openstreetmap.org/?mlat=59.61559&amp;mlon=17.83362#map=17/59.61559/17.83362">Here</a>, I copped out and just dropped nodes in approximate locations (most of those buildings have two entrances, on opposite sides, for each number). Is that better?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-housenumbers" rel="tag" title="see questions tagged &#39;housenumbers&#39;">housenumbers</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>29 Mar '17, 08:06</strong></p>
<img src="https://secure.gravatar.com/avatar/80abc4597de5aeb507c5a7ccd4ccee7a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="turepalsson&#39;s gravatar image" />
<p><span>turepalsson</span><br />
<span class="score" title="836 reputation points">836</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="25 badges"><span class="bronze">●</span><span class="badgecount">25</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="turepalsson has 3 accepted answers">25%</span></p>
</div>
</div>
<div id="comments-container-55321" class="comments-container">
<span id="55334"></span>
<div id="comment-55334" class="comment">
<div id="post-55334-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Using Nomiatim looking for a number between 44-36 Kritstigen doesn't work. but 44 or 36 Kritstigen does, so i think there is a bug.</p>
</div>
<div id="comment-55334-info" class="comment-info">
<span class="comment-age">(29 Mar '17, 19:54)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="55335"></span>
<div id="comment-55335" class="comment">
<div id="post-55335-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I also put number nodes on a building which rendered ok. But they are not found by nominatim.</p>
</div>
<div id="comment-55335-info" class="comment-info">
<span class="comment-age">(29 Mar '17, 19:58)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-55321" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55321-form-container" class="comment-form-container">
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

<span id="55359"></span>

<div id="answer-container-55359" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55359-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55359-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-55359-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>If the house numbers correspond to entrances in the real world, then mapping the entrances and adding the address tags to these entrances is generally the best solution. (I know you excluded this in your question, but other readers might consider this option.)</p>
<p>If you want or need to add the address tags to the building itself, different mapping styles have been discussed in the past, with no clear preference:</p>
<ul>
<li>listing all the house numbers as a semicolon-separated list, such as with your example <code>addr:housenumber=91;93;95</code> (commas are also sometimes used)</li>
<li>using a range such as <code>addr:housenumber=91-95</code>, possibly combined with an addr:interpolation tag to make it clear that this should be interpreted as a range instead of a single number</li>
<li>using the <a href="https://wiki.openstreetmap.org/wiki/Proposed_features/AddrN">addrN proposal</a> if the street or other parts of the address are different, not just the number (note that this is just a draft at the moment)</li>
</ul>
<p>Placing unconnected nodes on top of the building isn't uncommon either, but while it can look ok on some maps, it doesn't have clearly defined semantics and (from personal experience) makes it easy for the data to become messed up when people move either the address or building without also moving the other.</p>
<p>There's a <a href="https://wiki.openstreetmap.org/wiki/Addresses#Buildings_with_multiple_house_numbers">relevant section of the wiki</a> that offers a glimpse of the ongoing debate, but no clear recommendations.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>30 Mar '17, 09:18</strong></p>
<img src="https://secure.gravatar.com/avatar/0626be5f46f32fce501353e8a5ec399c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Tordanik&#39;s gravatar image" />
<p><span>Tordanik</span><br />
<span class="score" title="11998 reputation points"><span>12.0k</span></span><span title="15 badges"><span class="badge1">●</span><span class="badgecount">15</span></span><span title="106 badges"><span class="silver">●</span><span class="badgecount">106</span></span><span title="147 badges"><span class="bronze">●</span><span class="badgecount">147</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Tordanik has 58 accepted answers">35%</span></p>
</div>
</div>
<div id="comments-container-55359" class="comments-container">
&#10;</div>
<div id="comment-tools-55359" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55359-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55330"></span>

<div id="answer-container-55330" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55330-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55330-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55330-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This example looks ok here <a href="https://www.openstreetmap.org/search?query=163-185%20jeavons%20lane#map=19/52.21058/-0.07114">https://www.openstreetmap.org/search?query=163-185%20jeavons%20lane#map=19/52.21058/-0.07114</a> but to find the houses with nominatim 165 jeavons lane doesn't work but 163-185 jeavons lane together does?? so we need more info on how to enter those numbers. For semi- detached pairs ( two houses joined ) a search works. more dense numbers are messy with two or three story flats. nominatim finds this one (of a pair_ "20, Drivers Avenue, Huntingdon CP (Hunts), Huntingdon, Cambridgeshire, East of England, England, PE29 1UP, United Kingdom" here <a href="http://www.openstreetmap.org/#map=19/52.33466/-0.17465">http://www.openstreetmap.org/#map=19/52.33466/-0.17465</a> The house numbering here works fine, try it. <a href="https://www.openstreetmap.org/way/159765075#map=18/44.74378/-63.46505">https://www.openstreetmap.org/way/159765075#map=18/44.74378/-63.46505</a> There a bit here on flats <a href="http://wiki.openstreetmap.org/wiki/Key:addr:flats">http://wiki.openstreetmap.org/wiki/Key:addr:flats</a></p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '17, 17:24</strong></p>
<img src="https://secure.gravatar.com/avatar/efa7ca36d4499200879223dc5ad5ecac?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="andy%20mackey&#39;s gravatar image" />
<p><span>andy mackey</span><br />
<span class="score" title="13238 reputation points"><span>13.2k</span></span><span title="87 badges"><span class="badge1">●</span><span class="badgecount">87</span></span><span title="143 badges"><span class="silver">●</span><span class="badgecount">143</span></span><span title="285 badges"><span class="bronze">●</span><span class="badgecount">285</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="andy mackey has 37 accepted answers">4%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Mar '17, 19:44</strong> </span></p>
</div>
</div>
<div id="comments-container-55330" class="comments-container">
<span id="55339"></span>
<div id="comment-55339" class="comment">
<div id="post-55339-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Not sure how it works in Sweden or the UK but here in Germany something like 163-185 Jeavons Lane would not indicate a range of individual numbers. Instad 163-185 would be the single number of the building. This happens for example if a larger building occupies several smaller plots, where smaller buildings would have received those single numbers. So the address would always be given as 163-185 Jeavons Lane, never as 163 Jeavons Lane or 165 Jeavons lane. That said I don't think a data consumer would be able to defferentiate if 163-185 is the actual number or indicates a collection of numbers in the same building. I wonder if interpolation (<a href="https://wiki.openstreetmap.org/wiki/Addresses#Using_interpolation)">https://wiki.openstreetmap.org/wiki/Addresses#Using_interpolation)</a> would be the right problem to address this issue, even if not used anlong a street but inside a single building.</p>
</div>
<div id="comment-55339-info" class="comment-info">
<span class="comment-age">(29 Mar '17, 21:27)</span> <span class="comment-user userinfo">TZorn</span>
</div>
</div>
<span id="55360"></span>
<div id="comment-55360" class="comment">
<div id="post-55360-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Exactly what we do in Nottingham, if its a range of numbers we add addr:interpolation with either addr:housenumber or addr:flats ( most common case).</p>
</div>
<div id="comment-55360-info" class="comment-info">
<span class="comment-age">(30 Mar '17, 09:28)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
<span id="55364"></span>
<div id="comment-55364" class="comment">
<div id="post-55364-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have just tagged a five house terrace. We will probably have to wait to see if this address is found by nominatim. Try this address 111 thongsley huntingdon</p>
</div>
<div id="comment-55364-info" class="comment-info">
<span class="comment-age">(30 Mar '17, 12:29)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
<span id="55365"></span>
<div id="comment-55365" class="comment">
<div id="post-55365-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>That was quick ( 10 mins) 105 or 113 work but 107, 109 or 111, the ones in between don't. YET</p>
</div>
<div id="comment-55365-info" class="comment-info">
<span class="comment-age">(30 Mar '17, 12:33)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-55330" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55330-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55341"></span>

<div id="answer-container-55341" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55341-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55341-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-55341-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>How about creating several adress nodes and putting them at the same location? As long as they are within the boundaries of the building it should make sense.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '17, 21:50</strong></p>
<img src="https://secure.gravatar.com/avatar/f882e7865ffe23339fbaa71c9f576065?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredrikLindseth&#39;s gravatar image" />
<p><span>FredrikLindseth</span><br />
<span class="score" title="815 reputation points">815</span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="35 badges"><span class="bronze">●</span><span class="badgecount">35</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredrikLindseth has 2 accepted answers">13%</span></p>
</div>
</div>
<div id="comments-container-55341" class="comments-container">
<span id="55358"></span>
<div id="comment-55358" class="comment">
<div id="post-55358-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>It may look ok on the map if there isn't too many numbers but if you try nominatim address search including a number it does not find these terraces, but without a number it does work. <a href="http://www.openstreetmap.org/search?query=OCTAVIA%20TERRACE%20HUNTINGDON#map=18/52.34012/-0.16779">http://www.openstreetmap.org/search?query=OCTAVIA%20TERRACE%20HUNTINGDON#map=18/52.34012/-0.16779</a></p>
</div>
<div id="comment-55358-info" class="comment-info">
<span class="comment-age">(30 Mar '17, 08:31)</span> <span class="comment-user userinfo">andy mackey</span>
</div>
</div>
</div>
<div id="comment-tools-55341" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55341-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="55322"></span>

<div id="answer-container-55322" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-55322-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-55322-score" class="post-score" title="current number of votes">
-2
</div>
<span id="post-55322-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi turepalsson, take a look here, <a href="https://www.openstreetmap.org/#map=17/51.83893/4.95016">https://www.openstreetmap.org/#map=17/51.83893/4.95016</a> There are 2 ways, depending on the time or trouble the mapper puts into it. If you add all the numbers be sure to add the tag entrance=main and IMHO try to select the numbers around that entrance there and another group elsewhere based on local knowledge. The long building / apartments in the middle has as visible on the roof top 4 entrances. Take a look at the north- east corner, there is the same kind of building with the address nodes in groups near the entrances, the ideal situation.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>29 Mar '17, 10:58</strong></p>
<img src="https://secure.gravatar.com/avatar/742e93034cd38ad243f7ab26f350b659?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Hendrikklaas&#39;s gravatar image" />
<p><span>Hendrikklaas</span><br />
<span class="score" title="9286 reputation points"><span>9.3k</span></span><span title="207 badges"><span class="badge1">●</span><span class="badgecount">207</span></span><span title="238 badges"><span class="silver">●</span><span class="badgecount">238</span></span><span title="387 badges"><span class="bronze">●</span><span class="badgecount">387</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Hendrikklaas has 39 accepted answers">5%</span></p>
</div>
</div>
<div id="comments-container-55322" class="comments-container">
<span id="55323"></span>
<div id="comment-55323" class="comment">
<div id="post-55323-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>By Dijkstra’s beard, I thought Swedish house numbering was bad…! :-) Anyway, looks like "put nodes in approximately the right place".</p>
</div>
<div id="comment-55323-info" class="comment-info">
<span class="comment-age">(29 Mar '17, 11:06)</span> <span class="comment-user userinfo">turepalsson</span>
</div>
</div>
<span id="55329"></span>
<div id="comment-55329" class="comment">
<div id="post-55329-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>I'm not sure what the most ideal way would be to deal with this type of situation, but "randomly scatter address nodes in a blob inside the building outline" doesn't seem right to me. Thankfully this isn't how addressing works in Canada (generally the entire building would have one addr:housenumber), so I don't have to deal with it. :)</p>
</div>
<div id="comment-55329-info" class="comment-info">
<span class="comment-age">(29 Mar '17, 16:57)</span> <span class="comment-user userinfo">alester</span>
</div>
</div>
</div>
<div id="comment-tools-55322" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-55322-form-container" class="comment-form-container">
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

