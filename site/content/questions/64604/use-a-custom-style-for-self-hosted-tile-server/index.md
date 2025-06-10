+++
type = "question"
title = "Use a custom style for self-hosted tile server"
description = '''Hi guys, I&#x27;ve followed the instructions on switch2osm but couldn&#x27;t find any informations about how to use a different style. In the past we used openmaptiles and the style klokantech-basic but I haven&#x27;t found a way to use it on our own tile server (I don&#x27;t think it is possible at all, but maybe I&#x27;m ...'''
date = "2018-07-09T15:54:00Z"
lastmod = "2018-07-10T10:30:00Z"
weight = 64604
keywords = [ "tiles", "switch2osm", "style", "customization", "tileserver" ]
aliases = [ "/questions/64604" ]
osqa_answers = 1
osqa_accepted = true
+++

<div class="headNormal">

# [Use a custom style for self-hosted tile server](/questions/64604/use-a-custom-style-for-self-hosted-tile-server)

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
<span id="post-64604-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64604-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-64604-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi guys,</p>
<p>I've followed the instructions on <a href="https://switch2osm.org/manually-building-a-tile-server-18-04-lts/">switch2osm</a> but couldn't find any informations about how to use a different style. In the past we used openmaptiles and the style <a href="https://openmaptiles.org/styles/#klokantech-basic">klokantech-basic</a> but I haven't found a way to use it on our own tile server (I don't think it is possible at all, but maybe I'm wrong...).</p>
<p>Is there any tutorial on how to switch to a different style and eventually a website referencing some compatibles styles?</p>
<p>From what I understood, the openstreeetmap-carto style is not juste a style, some of its files are called during the setting-up process described on switch2osm (a .lua and .style file, etc.) so I'm also wondering how I'm supposed to use style like osm-bright for example (even if I'm looking for a much more simple one like klokantech-basic)?</p>
<p>Thanks a lot!</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-switch2osm" rel="tag" title="see questions tagged &#39;switch2osm&#39;">switch2osm</span> <span class="post-tag tag-link-style" rel="tag" title="see questions tagged &#39;style&#39;">style</span> <span class="post-tag tag-link-customization" rel="tag" title="see questions tagged &#39;customization&#39;">customization</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>09 Jul '18, 15:54</strong></p>
<img src="https://secure.gravatar.com/avatar/32a7da9bf999cc0ea4f6befea00edd8d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="voharunado&#39;s gravatar image" />
<p><span>voharunado</span><br />
<span class="score" title="66 reputation points">66</span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="10 badges"><span class="bronze">●</span><span class="badgecount">10</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="voharunado has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-64604" class="comments-container">
<span id="64607"></span>
<div id="comment-64607" class="comment">
<div id="post-64607-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The Klokantech map styles require fundamentally different software (and a fundamentally different approach to creating map tiles) to work compared to the OSM Carto style that switch2osm (and the OSM website) uses. If you want to use a Klokantech style you'll need to rely on information from them.</p>
</div>
<div id="comment-64607-info" class="comment-info">
<span class="comment-age">(09 Jul '18, 16:49)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64609"></span>
<div id="comment-64609" class="comment">
<div id="post-64609-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks for that info! Do you have any tutorial to use another style and eventualy a place where I could find some? Thanks!</p>
</div>
<div id="comment-64609-info" class="comment-info">
<span class="comment-age">(09 Jul '18, 17:07)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="64628"></span>
<div id="comment-64628" class="comment">
<div id="post-64628-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>A <a href="https://github.com/search?utf8=%E2%9C%93&amp;q=project+extension%3Amml&amp;type=Code&amp;ref=searchresults">github search</a> will find a number of projects with an mml file in them. Many of those will be Carto map styles. Not all will work with the same database though.</p>
</div>
<div id="comment-64628-info" class="comment-info">
<span class="comment-age">(10 Jul '18, 10:13)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="64632"></span>
<div id="comment-64632" class="comment">
<div id="post-64632-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I've found the kind of style I was looking for, compatible with osm-bright, I'll used that instead. Thanks for your help!</p>
</div>
<div id="comment-64632-info" class="comment-info">
<span class="comment-age">(10 Jul '18, 10:30)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
</div>
<div id="comment-tools-64604" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64604-form-container" class="comment-form-container">
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

<span id="64612"></span>

<div id="answer-container-64612" class="answer accepted-answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-64612-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-64612-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-64612-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span class="accept-answer on" rel="nofollow" title="voharunado has selected this answer as the correct answer"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>There isn't a public repository where you can pick a style and install it. There are some open source styles for Mapnik and a standard osm2pgsql database load around, notably (apart from openstreetmap-carto) <a href="https://github.com/mapbox/osm-bright,">https://github.com/mapbox/osm-bright,</a> <a href="https://github.com/der-stefan/OpenTopoMap,">https://github.com/der-stefan/OpenTopoMap,</a> and <a href="https://github.com/giggls/openstreetmap-carto-de">https://github.com/giggls/openstreetmap-carto-de</a> - but depending on which version of openstreetmap-carto you set up the database for, they might require small changes to the styles (or the database tables) - see also <a href="https://help.openstreetmap.org/questions/64602/how-to-specify-multiple-style-file-with-osm2pgsql-query">How to specify multiple style file with osm2pgsql query</a> for the travails of someone trying to run various styles off the same database schema!</p>
<p>If you want to use the Klokantech styles you need to install their backend rendering toolchain which is also open source, but different from what is discussed in switch2osm.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 Jul '18, 18:52</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>09 Jul '18, 18:54</strong> </span></p>
</div>
</div>
<div id="comments-container-64612" class="comments-container">
<span id="64625"></span>
<div id="comment-64625" class="comment">
<div id="post-64625-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Thanks Frederik! What I don't understand is the difference between osm-carto and osm-bright for example. Aren't they both styles for the tile server? I can use only one of them right? My installation is new and still in dev, so I can start again from sratch with osm-bright and the <a href="https://github.com/stekhn/blossom">blossom style</a> based on it? If I choose to use only this style, do I still need osm-carto? I don't understood this part of your answer...</p>
<p>By following the install instructions of osm-bright and converting the style with carto I should be able to use blossom? Or is there a part I didn't understood?</p>
<p>Thanks!</p>
</div>
<div id="comment-64625-info" class="comment-info">
<span class="comment-age">(10 Jul '18, 09:49)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="64626"></span>
<div id="comment-64626" class="comment">
<div id="post-64626-score" class="comment-score">
3
</div>
<div class="comment-text">
<p>Thing is, you have to load the data into PostGIS and there are many ways of doing that. You will find some "Toner Lite" styles on GitHub for example that are made for a database structure like the one generated by the importer "imposm", and they will not work with an import performed by osm2pgsql. Even two imports with osm2pgsql need not be compatible; one could for example use the hstore extension and the other not, or one could have used lua tag transforms to convert a column into integers and the other not. If both styles are for an osm2pgsql import then they will at least agree on which tables there are, and if they expect the columns to be subtly different then it should be possible to modify the styles with relative ease, or write database views that make the database look right for every style.</p>
</div>
<div id="comment-64626-info" class="comment-info">
<span class="comment-age">(10 Jul '18, 09:59)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64627"></span>
<div id="comment-64627" class="comment">
<div id="post-64627-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Ok I think I got it (correct me if I'm wrong please): if I start a new installation following osm-bright instructions to populate my dabatase, I won't need osm-carto and while I use only osm-bright compatible style it should work.</p>
</div>
<div id="comment-64627-info" class="comment-info">
<span class="comment-age">(10 Jul '18, 10:12)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
<span id="64629"></span>
<div id="comment-64629" class="comment">
<div id="post-64629-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Yes, osm-carto and osm-bright are different projects and you can run osm-bright without osm-carto.</p>
</div>
<div id="comment-64629-info" class="comment-info">
<span class="comment-age">(10 Jul '18, 10:14)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="64631"></span>
<div id="comment-64631" class="comment">
<div id="post-64631-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Great thanks a lot!</p>
</div>
<div id="comment-64631-info" class="comment-info">
<span class="comment-age">(10 Jul '18, 10:28)</span> <span class="comment-user userinfo">voharunado</span>
</div>
</div>
</div>
<div id="comment-tools-64612" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-64612-form-container" class="comment-form-container">
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

