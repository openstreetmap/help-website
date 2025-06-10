+++
type = "question"
title = "How can I import POIs from a PostGIS database into OpenStreetMap?"
description = '''Hi everybody, I need some help! I have a database in postgis with a lot of points about important places of my city. How can I import this data to OpenStreet? Do I use a .CSV file? How many fields can I get in the archive?  Can I create new datatypes, like &#x27;culture&#x27;s houses&#x27;? Thanks Fred'''
date = "2011-05-02T23:40:00Z"
lastmod = "2011-05-05T17:22:00Z"
weight = 4936
keywords = [ "import", "postgis", "poi" ]
aliases = [ "/questions/4936" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [How can I import POIs from a PostGIS database into OpenStreetMap?](/questions/4936/how-can-i-import-pois-from-a-postgis-database-into-openstreetmap)

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
<span id="post-4936-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4936-score" class="post-score" title="current number of votes">
8
</div>
<span id="post-4936-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi everybody, I need some help! I have a database in postgis with a lot of points about important places of my city. How can I import this data to OpenStreet? Do I use a .CSV file? How many fields can I get in the archive? Can I create new datatypes, like 'culture's houses'? Thanks Fred</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-import" rel="tag" title="see questions tagged &#39;import&#39;">import</span> <span class="post-tag tag-link-postgis" rel="tag" title="see questions tagged &#39;postgis&#39;">postgis</span> <span class="post-tag tag-link-poi" rel="tag" title="see questions tagged &#39;poi&#39;">poi</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>02 May '11, 23:40</strong></p>
<img src="https://secure.gravatar.com/avatar/4898e2af9ddc21fd1de1edd80b8cf7dc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="FredSoares&#39;s gravatar image" />
<p><span>FredSoares</span><br />
<span class="score" title="151 reputation points">151</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="FredSoares has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>29 Aug '13, 11:30</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0c12497903c6f3b2dd9f4d87deb127de?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="MagicFab&#39;s gravatar image" />
<p><span>MagicFab</span><br />
<span class="score" title="935 reputation points">935</span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="22 badges"><span class="bronze">●</span><span class="badgecount">22</span></span></p>
</div>
</div>
<div id="comments-container-4936" class="comments-container">
&#10;</div>
<div id="comment-tools-4936" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4936-form-container" class="comment-form-container">
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

<span id="4941"></span>

<div id="answer-container-4941" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-4941-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-4941-score" class="post-score" title="current number of votes">
15
</div>
<span id="post-4941-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There are a couple of questions that you should answer before thinking about the technical aspect of the import:</p>
<ol>
<li>Am I allowed to use the data and publish it under CC-BY-SA as well as under ODbL?</li>
<li>Is the data set accurate and useful?</li>
<li>Does the local community want the import</li>
<li>Do I have the technical abilities to cleanly conduct the import?</li>
<li>Does the data set conflict with existing data in OpenStreetMap?</li>
</ol>
<p>The first four question determine if you should import the data at all and the fifth one has a large influence on the way to do it.</p>
<p>About the import itself there are many way, some of which I'll give here, roughly ordered by amount of manual work:</p>
<ul>
<li>Tracing from custom images uses as background</li>
<li>Creating XML and manually copying from one layer to another in JOSM</li>
<li>Creating XML and automatically merge with exisiting data, check with JOSM and upload</li>
<li>Custom upload script</li>
</ul>
<p>Please get clear answers to the questions listed above, especially #1 and #3 before proceeding with any import to OpenStreetMap. OpenStreetMap is not a dataset dumping ground nor an aerial tracing project but an outdoor activity.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>03 May '11, 05:40</strong></p>
<img src="https://secure.gravatar.com/avatar/465f344e31e8ba1be0e0401414815db0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="petschge&#39;s gravatar image" />
<p><span>petschge</span><br />
<span class="score" title="8279 reputation points"><span>8.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="73 badges"><span class="silver">●</span><span class="badgecount">73</span></span><span title="98 badges"><span class="bronze">●</span><span class="badgecount">98</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="petschge has 29 accepted answers">21%</span></p>
</div>
</div>
<div id="comments-container-4941" class="comments-container">
<span id="4959"></span>
<div id="comment-4959" class="comment">
<div id="post-4959-score" class="comment-score">
5
</div>
<div class="comment-text">
<p>Before doing any imports, one should also carefully read the import guidelines on the wiki ( <a href="http://wiki.openstreetmap.org/wiki/Import/Guidelines">http://wiki.openstreetmap.org/wiki/Import/Guidelines</a> )</p>
<p>Imports can be a valuable source for improving the data in openstreetmap, but as with any mass edits, it also has a big potential to cause problems. This is why you will see many caution statements when discussing imports. Possibly the most important aspect is to make sure to discuss the import and technical details of the import beforehand. This allows people to give you "best practice" tips of how to do the import well.</p>
</div>
<div id="comment-4959-info" class="comment-info">
<span class="comment-age">(03 May '11, 16:42)</span> <span class="comment-user userinfo">apmon</span>
</div>
</div>
<span id="4973"></span>
<div id="comment-4973" class="comment">
<div id="post-4973-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>petschge, I'm a newbie in the OSM and do not want to disrespect the work of committed people here. I think that your questions are very important, to elevate the discussion about the OSM. To agregate the discussion It is important to answer your questions. I'm Geographer and the data that I want publicate came from my master's degree work. So there are no problems with the license or with the acuracy. Its is very important to our comunity to publicate those informations and a few persons have the hability to do this. About my technical abilities, I will need study these importation. I choice OSM just because I believe in your proposition. Sorry my english not is good, Thanks for your answer.</p>
</div>
<div id="comment-4973-info" class="comment-info">
<span class="comment-age">(03 May '11, 21:59)</span> <span class="comment-user userinfo">FredSoares</span>
</div>
</div>
<span id="4974"></span>
<div id="comment-4974" class="comment">
<div id="post-4974-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I'm very glad that there are good and clear answers to the questions I posed. If you add a comment to your question containing information about the format the data is currently in we can help you with the technical side of the import.</p>
</div>
<div id="comment-4974-info" class="comment-info">
<span class="comment-age">(03 May '11, 22:04)</span> <span class="comment-user userinfo">petschge</span>
</div>
</div>
<span id="4998"></span>
<div id="comment-4998" class="comment">
<div id="post-4998-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Thanks apmon and ptschge. I'm very happy with your answers. ptschge, thanks a lot for offering to help in the import process. I have a DB postgis whith SRID 4326. I want import two 'views' with the same datatype: POINT. Encoding UTF8 Below the description of views.</p>
<p>First one is about the places who the local community gathers to do culture, its is very dificult translate this. See more on Youtube 'Cartografia da Cultura Candanga'</p>
<p>View name: entidades_culturais.</p>
<p>columns: id (integer), name (character varying 255), adress (character varying 255), activity (text), contacts (character varying 255), midia (contain youtube's url (character varying 255)) the_geom.</p>
<p>The second view contains the position and description about all public equipament's cultural of city - museums, theatres, libraries, cinemas and places to music shows.</p>
<p>View name: equipamentos_culturais</p>
<p>columns: id (integer), name (character varying 255), type (This column describes the kind of place, it have five kinds: museum, theatres... - (character varying 255)), adress (character varying 255), contacts (character varying 255), the_geom.</p>
<p>I hope that was the information that you asked for. How we can import those data? Do we use a .CSV file? Sorry again, my english not is good. Thanks</p>
</div>
<div id="comment-4998-info" class="comment-info">
<span class="comment-age">(05 May '11, 02:20)</span> <span class="comment-user userinfo">FredSoares</span>
</div>
</div>
<span id="4999"></span>
<div id="comment-4999" class="comment">
<div id="post-4999-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Fred, it's great that you're enthusiastic about contributing to OpenStreetMap, but you really should not be considering an import any time soon. You have much to learn about OSM before you can make such a large edit.</p>
<p>Your description of columns, views and the like has no relevance to OSM. OSM's data structure does not work anything like that. You certainly cannot use a CSV file.</p>
<p>More seriously, the challenge with imports is not primarily technical, but a community challenge. You need to talk to local mappers and check that they are happy.</p>
<p>I suggest that you sign up to your local mailing list (see <a href="http://lists.openstreetmap.org/listinfo">http://lists.openstreetmap.org/listinfo</a> for a full list) and talk to the existing mappers in the country. Some of them might have technical expertise and be able to carry out the import, if they consider it desirable, in an effective way. You should also sign up to the dedicated imports mailing list.</p>
</div>
<div id="comment-4999-info" class="comment-info">
<span class="comment-age">(05 May '11, 12:43)</span> <span class="comment-user userinfo">Richard ♦</span>
</div>
</div>
</div>
<div id="comment-tools-4941" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-4941-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="5004"></span>

<div id="answer-container-5004" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-5004-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-5004-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-5004-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>We're talking about <a href="http://www.openstreetmap.org/?lat=-15.85229&amp;lon=-47.94951&amp;zoom=16&amp;layers=M">here</a>, right? Currently the OSM map has the town/suburb label, but no streets (or anything else). Whilst it's useful to know where individual points of interest are on the map, it's useful to know that in the context of where everything else is, in particular streets - I'm not convinced that a scatter of "Cultural Places" on an otherwise completely empty map would be of much use to anyone.</p>
<p>If however you have any GPS traces collected when going around Candangolândia, then it'd be really useful to upload those to OSM. Even if you're not going to do anything with them yourself, having on-the-ground GPS traces helps people adding features from aerial photos (e.g. the Bing layer) to work around any offset that there might be between aerial photos and what's actually on the ground. The suburb to the northwest (Guara) looks like it's been traced from aerial photos (there are no street names), so perhaps whoever did that might want to have a go at Candangolândia too? Try sending a mail to the talk-br list or mailing them via the OSM website.</p>
<p>In addition to GPS traces you might have other useful information (such as street names or other "non-cultural place" points of interest) for Candangolândia - it would be useful to make that available who's interested in mapping Candangolândia (preferably on the ground, but also remotely).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>05 May '11, 17:22</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-5004" class="comments-container">
&#10;</div>
<div id="comment-tools-5004" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-5004-form-container" class="comment-form-container">
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

