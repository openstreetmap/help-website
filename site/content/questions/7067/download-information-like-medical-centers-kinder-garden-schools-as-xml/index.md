+++
type = "question"
title = "Download information like medical centers, kinder garden, schools ... as XML"
description = '''Hi, I have an commercial project where I want to connect some information with interesting points like schools, police departments, POI&#x27;s, kinder gardens, medical centers etc. by given GEO coordinates for an radius of some miles. For this project I need to have worldwide the GEO coordinates of the d...'''
date = "2011-08-13T18:51:00Z"
lastmod = "2011-08-13T22:02:00Z"
weight = 7067
keywords = [ "download" ]
aliases = [ "/questions/7067" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Download information like medical centers, kinder garden, schools ... as XML](/questions/7067/download-information-like-medical-centers-kinder-garden-schools-as-xml)

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
<span id="post-7067-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7067-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7067-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, I have an commercial project where I want to connect some information with interesting points like schools, police departments, POI's, kinder gardens, medical centers etc. by given GEO coordinates for an radius of some miles. For this project I need to have worldwide the GEO coordinates of the different types of points. I have see that, this points are available in OpenStreet Map and I want to know if it's possible to download this information with the whole information and to use it for my commercial project? Is there an download are where I can choose what type of point I am interested. For example all medical centres in the world, all schools in the world etc.?</p>
<p>I will be very happy for some information!</p>
<p>Best Regards Nik</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-download" rel="tag" title="see questions tagged &#39;download&#39;">download</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>13 Aug '11, 18:51</strong></p>
<img src="https://secure.gravatar.com/avatar/62522b4bc4677a7a32b576449aa1a3e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nnikolay&#39;s gravatar image" />
<p><span>nnikolay</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nnikolay has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>13 Aug '11, 19:04</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span></p>
</div>
</div>
<div id="comments-container-7067" class="comments-container">
&#10;</div>
<div id="comment-tools-7067" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7067-form-container" class="comment-form-container">
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

<span id="7068"></span>

<div id="answer-container-7068" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7068-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7068-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-7068-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>For the first question, regarding making geographically bound queries about specific attributes, you should look at <a href="https://wiki.openstreetmap.org/wiki/Xapi">XAPI</a>, which allows you to ask for specific tags within a bounding box.</p>
<p>For the second part of your question:</p>
<blockquote>
<p>I want to know if it's possible to download this information with the whole information and to use it for my commercial project?</p>
</blockquote>
<p>I don't know what "this information with the whole information" means, but we have lots of documentation on the Wiki regarding how to use OSM data (attribution, and requirements for derived data). The best place to start is probably the <a href="https://wiki.openstreetmap.org/wiki/Legal_FAQ#Using">Legal FAQ</a>.</p>
<p>The basic answer is that OSM data is currently available under the terms of the Creative Commons CC-BY-SA license, and that means if you're using it with some other dataset, the entire dataset/map must be distributed under the terms of the CC-BY-SA license.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '11, 19:21</strong></p>
<img src="https://secure.gravatar.com/avatar/5f2082b86cc50d63c05f33f55166df2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="emacsen&#39;s gravatar image" />
<p><span>emacsen</span><br />
<span class="score" title="1191 reputation points"><span>1.2k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="23 badges"><span class="bronze">●</span><span class="badgecount">23</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="emacsen has 4 accepted answers">13%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>15 Aug '11, 02:21</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/aa505c046b1c010e997a7849c6f3dbbe?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Vclaw&#39;s gravatar image" />
<p><span>Vclaw</span><br />
<span class="score" title="9217 reputation points"><span>9.2k</span></span><span title="8 badges"><span class="badge1">●</span><span class="badgecount">8</span></span><span title="95 badges"><span class="silver">●</span><span class="badgecount">95</span></span><span title="141 badges"><span class="bronze">●</span><span class="badgecount">141</span></span></p>
</div>
</div>
<div id="comments-container-7068" class="comments-container">
<span id="7069"></span>
<div id="comment-7069" class="comment">
<div id="post-7069-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Instead of the old XAPI one should use the new <a href="https://wiki.openstreetmap.org/wiki/Overpass_API">Overpass API</a> which is more flexible and less broken.</p>
</div>
<div id="comment-7069-info" class="comment-info">
<span class="comment-age">(13 Aug '11, 19:33)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="7070"></span>
<div id="comment-7070" class="comment">
<div id="post-7070-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Alex, I disagree regarding Overpass, for multiple reasons (and I do not think XAPI is broken. help isn't a place for debate, and we can discuss this on another forum.</p>
</div>
<div id="comment-7070-info" class="comment-info">
<span class="comment-age">(13 Aug '11, 19:44)</span> <span class="comment-user userinfo">emacsen</span>
</div>
</div>
<span id="7074"></span>
<div id="comment-7074" class="comment">
<div id="post-7074-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, is there some example, how to get from the Overpass API or the XAPI all schools in Berlin, for example?</p>
</div>
<div id="comment-7074-info" class="comment-info">
<span class="comment-age">(13 Aug '11, 21:47)</span> <span class="comment-user userinfo">nnikolay</span>
</div>
</div>
</div>
<div id="comment-tools-7068" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7068-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="7071"></span>

<div id="answer-container-7071" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-7071-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-7071-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-7071-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Hi, thanks for the answers! I have see the Creative Commons CC-BY-SA license it is ok! I will not sell the data or something! I will only display some additional inforation in radius of 50 km or miles to some of my properties what I am displaying on my site.</p>
<p>Where can I download the information and the another importand think is, how can I extract for example only the restaurants, mediacal centers, schools etc? Is there a list o all tags how can I extract the info?</p>
<p>Thanks Nik</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Aug '11, 20:46</strong></p>
<img src="https://secure.gravatar.com/avatar/62522b4bc4677a7a32b576449aa1a3e8?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="nnikolay&#39;s gravatar image" />
<p><span>nnikolay</span><br />
<span class="score" title="16 reputation points">16</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="3 badges"><span class="bronze">●</span><span class="badgecount">3</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="nnikolay has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-7071" class="comments-container">
<span id="7072"></span>
<div id="comment-7072" class="comment">
<div id="post-7072-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Nik,</p>
<p>help is not a forum for ongoing discussions, but rather it's a question/answer system ala StackOverflow. Please use the mailing lists, IRC or forums for this kind of help.</p>
</div>
<div id="comment-7072-info" class="comment-info">
<span class="comment-age">(13 Aug '11, 20:51)</span> <span class="comment-user userinfo">emacsen</span>
</div>
</div>
<span id="7073"></span>
<div id="comment-7073" class="comment">
<div id="post-7073-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>For a list of tags please take a look at our wiki, everything else has already been said.</p>
</div>
<div id="comment-7073-info" class="comment-info">
<span class="comment-age">(13 Aug '11, 21:09)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="7075"></span>
<div id="comment-7075" class="comment">
<div id="post-7075-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Scai, I have found the tags, but it will be great to have an example for example all schools in Berlin. Is there some example?</p>
</div>
<div id="comment-7075-info" class="comment-info">
<span class="comment-age">(13 Aug '11, 21:49)</span> <span class="comment-user userinfo">nnikolay</span>
</div>
</div>
<span id="7076"></span>
<div id="comment-7076" class="comment">
<div id="post-7076-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Just use amenity=school and the bounding box of Berlin. If the bounding box is too rough you can also use osmosis afterwards with a polygon filter. Example usages can be found on the wiki pages of XAPI and Overpass. If you have more questions it might be better to use our forum or mailing lists.</p>
</div>
<div id="comment-7076-info" class="comment-info">
<span class="comment-age">(13 Aug '11, 22:02)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
</div>
<div id="comment-tools-7071" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-7071-form-container" class="comment-form-container">
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

