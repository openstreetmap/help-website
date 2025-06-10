+++
type = "question"
title = "Restaurant names that begins with Chinese characters do not render on main map"
description = '''Hi I found a very strange behavior with the rendering of restaurant names. If the main name begins with Latin letters (https://www.openstreetmap.org/node/2473232920 or https://www.openstreetmap.org/node/2473232930), then the name renders, even if there are Chinese characters that follow. If the main...'''
date = "2014-09-16T23:54:00Z"
lastmod = "2014-09-18T08:51:00Z"
weight = 36870
keywords = [ "rendering", "chinese", "restaurants" ]
aliases = [ "/questions/36870" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [Restaurant names that begins with Chinese characters do not render on main map](/questions/36870/restaurant-names-that-begins-with-chinese-characters-do-not-render-on-main-map)

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
<span id="post-36870-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36870-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-36870-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi</p>
<p>I found a very strange behavior with the rendering of restaurant names. If the main name begins with Latin letters (<a href="https://www.openstreetmap.org/node/2473232920">https://www.openstreetmap.org/node/2473232920</a> or <a href="https://www.openstreetmap.org/node/2473232930">https://www.openstreetmap.org/node/2473232930</a>), then the name renders, even if there are Chinese characters that follow. If the main name begins with a Chinese character (<a href="https://www.openstreetmap.org/node/2473232927">https://www.openstreetmap.org/node/2473232927</a>), then the name does not render.</p>
<p>This does not happen with other types of node, like convenient stores. The same happens when my language setting is</p>
<p>zh-TW,zh,en-US,en or zh,en-US,en or en</p>
<p>Is this a bug to be fixed?</p>
<p>Thanks</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-rendering" rel="tag" title="see questions tagged &#39;rendering&#39;">rendering</span> <span class="post-tag tag-link-chinese" rel="tag" title="see questions tagged &#39;chinese&#39;">chinese</span> <span class="post-tag tag-link-restaurants" rel="tag" title="see questions tagged &#39;restaurants&#39;">restaurants</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>16 Sep '14, 23:54</strong></p>
<img src="https://secure.gravatar.com/avatar/73aa0ab67ea59bdf1f2514d129f8331a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="fosius_luminis&#39;s gravatar image" />
<p><span>fosius_luminis</span><br />
<span class="score" title="31 reputation points">31</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="fosius_luminis has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>17 Sep '14, 07:41</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</div>
</div>
<div id="comments-container-36870" class="comments-container">
<span id="36873"></span>
<div id="comment-36873" class="comment">
<div id="post-36873-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Is it perhaps just a label placement issue (i.e. the renderer thinks that it hasn't got room for the Chinese name for "Discovery Noodle" and leaves it out? On my tile server at home (similar mapnik version, slightly older version of the OSM "standard" style, but only rendering recently added data, so that it omits <a href="https://www.openstreetmap.org/way/49698363">way 49698363</a>) it does try and display the Chinese "Discovery Noodle" name. Can you find another example where the Chinese restaurant name definitely wouldn't run across another feature?</p>
</div>
<div id="comment-36873-info" class="comment-info">
<span class="comment-age">(17 Sep '14, 07:52)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="36884"></span>
<div id="comment-36884" class="comment">
<div id="post-36884-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Here are some nodes that have nothing below them</p>
<p><a href="https://www.openstreetmap.org/node/2473232960">https://www.openstreetmap.org/node/2473232960</a> <a href="https://www.openstreetmap.org/node/2579109207">https://www.openstreetmap.org/node/2579109207</a> <a href="https://www.openstreetmap.org/node/2812986184">https://www.openstreetmap.org/node/2812986184</a> <a href="https://www.openstreetmap.org/node/2921833439">https://www.openstreetmap.org/node/2921833439</a></p>
<p>although there are some counter-examples <a href="https://www.openstreetmap.org/node/2151389193">https://www.openstreetmap.org/node/2151389193</a> <a href="https://www.openstreetmap.org/node/2473232863">https://www.openstreetmap.org/node/2473232863</a> (only shows at zoom level 17)</p>
<p>But most fall into the "broken" category.</p>
</div>
<div id="comment-36884-info" class="comment-info">
<span class="comment-age">(17 Sep '14, 17:37)</span> <span class="comment-user userinfo">fosius_luminis</span>
</div>
</div>
<span id="36885"></span>
<div id="comment-36885" class="comment">
<div id="post-36885-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Interesting (for info, my tile server does try to display all the names that I'd expect it to, although it doesn't have Chinese fonts loaded). As Pieren suggests, I'd log it as a Github issue against the stylesheet.</p>
<p>If you don't have a github account let me know, and I'll log an issue cross-referencing this question.</p>
</div>
<div id="comment-36885-info" class="comment-info">
<span class="comment-age">(17 Sep '14, 17:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="36886"></span>
<div id="comment-36886" class="comment">
<div id="post-36886-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't have a github account. If you could do that for me, that'd be great! Thanks!</p>
</div>
<div id="comment-36886-info" class="comment-info">
<span class="comment-age">(17 Sep '14, 18:55)</span> <span class="comment-user userinfo">fosius_luminis</span>
</div>
</div>
<span id="36895"></span>
<div id="comment-36895" class="comment">
<div id="post-36895-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>I've created <a href="https://github.com/gravitystorm/openstreetmap-carto/issues/959">https://github.com/gravitystorm/openstreetmap-carto/issues/959</a></p>
</div>
<div id="comment-36895-info" class="comment-info">
<span class="comment-age">(18 Sep '14, 08:51)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-36870" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36870-form-container" class="comment-form-container">
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

One Answer:

</div>

</div>

<span id="36883"></span>

<div id="answer-container-36883" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-36883-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-36883-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-36883-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>It seems that the street names are correctly rendered in Chinese fonts but not the restaurant names. This sounds as a rendering issue with Mapnik or its stylesheet. I would suggest to submit an error report (issue) on the Mapnik stylesheet development repository : <a href="https://github.com/gravitystorm/openstreetmap-carto">https://github.com/gravitystorm/openstreetmap-carto</a> (guess you need a github user account)</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>17 Sep '14, 16:48</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-36883" class="comments-container">
&#10;</div>
<div id="comment-tools-36883" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-36883-form-container" class="comment-form-container">
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

