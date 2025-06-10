+++
type = "question"
title = "Proper piste:type values to use?"
description = '''In preparation for generating a new map of an area I ski, I am adding the trail data to OSM. And I have become confused as to the proper piste:type values to use. Most trails are over old logging drags or are marked with metal tags attached to trees and are easily followed in summer (hiking) or wint...'''
date = "2013-03-27T00:18:00Z"
lastmod = "2013-03-27T21:51:00Z"
weight = 21015
keywords = [ "trail", "piste", "types" ]
aliases = [ "/questions/21015" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [Proper piste:type values to use?](/questions/21015/proper-pistetype-values-to-use)

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
<span id="post-21015-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21015-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-21015-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>In preparation for generating a new map of an area I ski, I am adding the trail data to OSM. And I have become confused as to the proper piste:type values to use.</p>
<p>Most trails are over old logging drags or are marked with metal tags attached to trees and are easily followed in summer (hiking) or winter (cross country skiing). I've tagged those as piste:type=nordic with piste:grooming=backcountry. They are used by people on classic, light weight, nordic ski gear.</p>
<p>However there are a number of "trails" that are "general direction suggestions". They do not follow obvious old road cuts or clearings (but may follow a drainage or ridge). These are unflagged and unmarked in the field. These "trails" are usually used by people using heavier telemark type gear.</p>
<p>It looks like the piste:type=skitour might be the appropriate tag for these "general direction" "trails" but the wiki page at <a href="https://wiki.openstreetmap.org/wiki/Key%3Apiste%3Atype">https://wiki.openstreetmap.org/wiki/Key%3Apiste%3Atype</a> refers to <a href="https://en.wikipedia.org/wiki/Ski_touring">https://en.wikipedia.org/wiki/Ski_touring</a> and the description there would actually fit all of the trails.</p>
<p>What piste:type value should I use for these? Or should I even add them to the OSM database at all?</p>
<p>I don't need an answer immediately as the recommended route for some of these has changed since I last got GPS tracks and I need to do some new field work before I can enter them, but when I get there I would like to know what to do on them.</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-trail" rel="tag" title="see questions tagged &#39;trail&#39;">trail</span> <span class="post-tag tag-link-piste" rel="tag" title="see questions tagged &#39;piste&#39;">piste</span> <span class="post-tag tag-link-types" rel="tag" title="see questions tagged &#39;types&#39;">types</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>27 Mar '13, 00:18</strong></p>
<img src="https://secure.gravatar.com/avatar/f60af53a4eba0c21f25c22674fb4a8cc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="n76&#39;s gravatar image" />
<p><span>n76</span><br />
<span class="score" title="10839 reputation points"><span>10.8k</span></span><span title="10 badges"><span class="badge1">●</span><span class="badgecount">10</span></span><span title="82 badges"><span class="silver">●</span><span class="badgecount">82</span></span><span title="172 badges"><span class="bronze">●</span><span class="badgecount">172</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="n76 has 48 accepted answers">17%</span></p>
</div>
</div>
<div id="comments-container-21015" class="comments-container">
&#10;</div>
<div id="comment-tools-21015" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21015-form-container" class="comment-form-container">
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

<span id="21021"></span>

<div id="answer-container-21021" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21021-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21021-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-21021-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="n76 has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>As always the best way to understand the generally accepted meaning of a tag is to examine existing usage. Taginfo shows that <code>piste:type=skitour</code> has been used <a href="http://taginfo.openstreetmap.org/tags/piste%3Atype=skitour#overview">806 times</a> on OSM. Using the XAPI button on taginfo I downloaded all these as an OSM XML file and inspected it in JOSM. The bulk of the usage is in the Alps, and the individual ways I checked are true alpine ski-tours, such as the ascent of the <a href="http://www.openstreetmap.org/browse/way/28832974">Strahlhorn</a>, or classic backcountry ski descents such as <a href="http://www.openstreetmap.org/browse/way/103548294">Teufi</a>. (Personally, I think this usage is overloaded, and that we still need better tagging to discriminate between these, they require completely different skills and experience).</p>
<p>You could examine usage of <code>piste:type=nordic</code> in a similar way to see if there are any areas where someone has already tagged similar ski routes to those you wish to map. I expect that, as with alpine skiing, the tagging scheme still has holes. If it does then feel free to suggest <strong>and use</strong> enhancements (contrary to much of what the wiki says tag usage is established by practice and example).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '13, 10:53</strong></p>
<img src="https://secure.gravatar.com/avatar/06cd84075f1adc2870ad102c7233e661?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SK53&#39;s gravatar image" />
<p><span>SK53 ♦</span><br />
<span class="score" title="28084 reputation points"><span>28.1k</span></span><span title="48 badges"><span class="badge1">●</span><span class="badgecount">48</span></span><span title="268 badges"><span class="silver">●</span><span class="badgecount">268</span></span><span title="433 badges"><span class="bronze">●</span><span class="badgecount">433</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SK53 has 121 accepted answers">22%</span></p>
</div>
</div>
<div id="comments-container-21021" class="comments-container">
<span id="21028"></span>
<div id="comment-21028" class="comment">
<div id="post-21028-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thank you. I've been checking taginfo to see the relative frequency of various usages but am a newbie at OSM and was unaware of the technique for digging deeper in to this to find the actual use cases for examination.</p>
</div>
<div id="comment-21028-info" class="comment-info">
<span class="comment-age">(27 Mar '13, 15:51)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
<span id="21036"></span>
<div id="comment-21036" class="comment">
<div id="post-21036-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I wonder if it's necessary to split piste:type=skitour with wikipedia described variants, but why not. Another way would be to use piste:difficulty to grade these, maybe with new values. One thing I'm quite sure off is that we shouldn't describe a piste by the gear required or commonly used on a particular trail, but rather from the experience and skills needed.</p>
</div>
<div id="comment-21036-info" class="comment-info">
<span class="comment-age">(27 Mar '13, 21:51)</span> <span class="comment-user userinfo">yvecai</span>
</div>
</div>
</div>
<div id="comment-tools-21021" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21021-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="21019"></span>

<div id="answer-container-21019" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-21019-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-21019-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-21019-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I've seen some pistes tagged piste:type=nordic, piste:grooming=backcountry. <a href="http://www.pistes-nordiques.org/?zoom=15&amp;lat=34.815&amp;lon=-119.11497">example</a></p>
<p>This would account for backcountry crosscountry skis, which or not the same gear used in alpine ski-touring.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>27 Mar '13, 07:10</strong></p>
<img src="https://secure.gravatar.com/avatar/3c7cffe544d6a1c46c97a25b2fdcdedc?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yvecai&#39;s gravatar image" />
<p><span>yvecai</span><br />
<span class="score" title="1481 reputation points"><span>1.5k</span></span><span title="12 badges"><span class="silver">●</span><span class="badgecount">12</span></span><span title="26 badges"><span class="bronze">●</span><span class="badgecount">26</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yvecai has 7 accepted answers">9%</span></p>
</div>
</div>
<div id="comments-container-21019" class="comments-container">
<span id="21027"></span>
<div id="comment-21027" class="comment">
<div id="post-21027-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for the link but that would be, in this case, not a good example as that is the area I am trying to update. For an example of the old map see <a href="http://www.nordicbase.org/maps">http://www.nordicbase.org/maps</a></p>
</div>
<div id="comment-21027-info" class="comment-info">
<span class="comment-age">(27 Mar '13, 15:47)</span> <span class="comment-user userinfo">n76</span>
</div>
</div>
</div>
<div id="comment-tools-21019" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-21019-form-container" class="comment-form-container">
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

