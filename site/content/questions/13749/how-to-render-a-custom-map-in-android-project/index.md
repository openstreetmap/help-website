+++
type = "question"
title = "how to render a custom map in android project?"
description = '''Hi people, I am running the OpenStreetMapViewer android project and I would like to render the map without places like restaurants, markets, etc. I know that it is possible but I am not sure how to do it . Anyone can help me?? Thanks in advance'''
date = "2012-06-24T21:54:00Z"
lastmod = "2013-05-10T13:16:00Z"
weight = 13749
keywords = [ "map", "osmdroid", "render", "custom" ]
aliases = [ "/questions/13749" ]
osqa_answers = 3
osqa_accepted = false
+++

<div class="headNormal">

# [how to render a custom map in android project?](/questions/13749/how-to-render-a-custom-map-in-android-project)

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
<span id="post-13749-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13749-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-13749-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi people, I am running the OpenStreetMapViewer android project and I would like to render the map without places like restaurants, markets, etc. I know that it is possible but I am not sure how to do it . Anyone can help me?? Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-map" rel="tag" title="see questions tagged &#39;map&#39;">map</span> <span class="post-tag tag-link-osmdroid" rel="tag" title="see questions tagged &#39;osmdroid&#39;">osmdroid</span> <span class="post-tag tag-link-render" rel="tag" title="see questions tagged &#39;render&#39;">render</span> <span class="post-tag tag-link-custom" rel="tag" title="see questions tagged &#39;custom&#39;">custom</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>24 Jun '12, 21:54</strong></p>
<img src="https://secure.gravatar.com/avatar/9865afb1c2b5b29755f3a83cedb890aa?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="gastolson&#39;s gravatar image" />
<p><span>gastolson</span><br />
<span class="score" title="26 reputation points">26</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="4 badges"><span class="bronze">●</span><span class="badgecount">4</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="gastolson has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-13749" class="comments-container">
<span id="13751"></span>
<div id="comment-13751" class="comment">
<div id="post-13751-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Would it be possible to post a link to the "OpenStreetMapViewer android project" that you're running? We don't know if it's a tile viewer, a data renderer, or something else...</p>
</div>
<div id="comment-13751-info" class="comment-info">
<span class="comment-age">(24 Jun '12, 22:15)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="13753"></span>
<div id="comment-13753" class="comment">
<div id="post-13753-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>sure! here I copy the link: <a href="http://code.google.com/p/osmdroid/.">http://code.google.com/p/osmdroid/.</a> I hope it helps you to understand.</p>
</div>
<div id="comment-13753-info" class="comment-info">
<span class="comment-age">(24 Jun '12, 22:58)</span> <span class="comment-user userinfo">gastolson</span>
</div>
</div>
</div>
<div id="comment-tools-13749" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13749-form-container" class="comment-form-container">
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

<span id="22264"></span>

<div id="answer-container-22264" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22264-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22264-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-22264-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I would suspect the by far best way to handle a custom map on Android is to use mapsforge <a href="http://code.google.com/p/mapsforge/">http://code.google.com/p/mapsforge/</a> It does have the disadvantage that the map data hast to be downloaded, but that is by far outweighed by the advantages.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 May '13, 13:16</strong></p>
<img src="https://secure.gravatar.com/avatar/ad2513d6f8e3d709d576ace900c12fa5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SimonPoole&#39;s gravatar image" />
<p><span>SimonPoole ♦</span><br />
<span class="score" title="44667 reputation points"><span>44.7k</span></span><span title="13 badges"><span class="badge1">●</span><span class="badgecount">13</span></span><span title="326 badges"><span class="silver">●</span><span class="badgecount">326</span></span><span title="701 badges"><span class="bronze">●</span><span class="badgecount">701</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SimonPoole has 209 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 May '13, 13:16</strong> </span></p>
</div>
</div>
<div id="comments-container-22264" class="comments-container">
&#10;</div>
<div id="comment-tools-22264" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-22264-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="13764"></span>

<div id="answer-container-13764" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-13764-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-13764-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-13764-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>This project seems to use existing tile servers (OpenStreetMap.org, cyclestreet) which are not customizable. If you have special needs, either check/contact one OSM tiles provider (list available on the wiki) or set-up your own tile server where you will be free to change styles and updates intervals.</p>
<p>Please search existing replies about 'how to render or customize my own map' on this help site, e.g. <a href="/questions/136/how-do-i-render-my-own-maps-for-my-website">this one</a>. Also check <a href="https://wiki.openstreetmap.org/wiki/Renderer">the wiki</a> reflecting the latest info about rendering OSM data (e.g. with TileMill).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>25 Jun '12, 15:19</strong></p>
<img src="https://secure.gravatar.com/avatar/0e92f2d89853fd4e04c4b40a921e519b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pieren&#39;s gravatar image" />
<p><span>Pieren</span><br />
<span class="score" title="9847 reputation points"><span>9.8k</span></span><span title="20 badges"><span class="badge1">●</span><span class="badgecount">20</span></span><span title="83 badges"><span class="silver">●</span><span class="badgecount">83</span></span><span title="157 badges"><span class="bronze">●</span><span class="badgecount">157</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pieren has 34 accepted answers">15%</span></p>
</div>
</div>
<div id="comments-container-13764" class="comments-container">
<span id="13865"></span>
<div id="comment-13865" class="comment">
<div id="post-13865-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I have been reading about some options to customize the map. As you said, this seems to use existing tile servers. What I really need is to change, if possible, the URL server with the same Android Project to retrieve "base" tiles. Do you consider this possible? Thanks</p>
</div>
<div id="comment-13865-info" class="comment-info">
<span class="comment-age">(27 Jun '12, 23:02)</span> <span class="comment-user userinfo">gastolson</span>
</div>
</div>
<span id="13908"></span>
<div id="comment-13908" class="comment">
<div id="post-13908-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>your question no longer seems to be an FAQ ... so feel invited do discuss more details at one of the OSM mailing lists (maybe about developing) or one of the forums at <a href="http://forum.osm.org">http://forum.osm.org</a></p>
</div>
<div id="comment-13908-info" class="comment-info">
<span class="comment-age">(29 Jun '12, 15:45)</span> <span class="comment-user userinfo">stephan75</span>
</div>
</div>
<span id="22215"></span>
<div id="comment-22215" class="comment">
<div id="post-22215-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><span>@gastolson</span> Did you figure out a way to change the URL server? Please tell because I also have the same problem. I have a working Mapserver using MS4W. I can render my map tiles to webbrowser. Now I need to connect it to my Android application using OSMDROID. Thanks in advance.</p>
</div>
<div id="comment-22215-info" class="comment-info">
<span class="comment-age">(09 May '13, 12:36)</span> <span class="comment-user userinfo">Hishan</span>
</div>
</div>
</div>
<div id="comment-tools-13764" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-13764-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="22216"></span>

<div id="answer-container-22216" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-22216-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-22216-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-22216-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>You'll need to create some tiles displaying only the information that you want, and then use those (online or more probably offline) in Osmdroid.</p>
<p>A quick web search found <a href="http://www.haakseth.com/?p=30">this tutorial</a> about configuring an Osmdroid project to work with offline tiles.</p>
<p>The process of creating the tiles is called "rendering" and there are many, many different options. I'd start with <a href="https://help.openstreetmap.org/search/?q=rendering&amp;Submit=Search&amp;t=question">a search for rendering questions on this help site</a>, and also <a href="https://wiki.openstreetmap.org/wiki/Rendering">this page on the OSM wiki</a>.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>09 May '13, 14:06</strong></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="SomeoneElse has 228 accepted answers">16%</span></p>
</div>
</div>
<div id="comments-container-22216" class="comments-container">
<span id="22219"></span>
<div id="comment-22219" class="comment">
<div id="post-22219-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>thanks <span>@SomeoneElse</span> for quick reply. In fact I read all the sites you have mentioned. And none of them explains how to use my MapServer implemented using MS4W. I also plan to display routes using given starting point and destination point. Can you help me with that?</p>
</div>
<div id="comment-22219-info" class="comment-info">
<span class="comment-age">(09 May '13, 15:09)</span> <span class="comment-user userinfo">Hishan</span>
</div>
</div>
<span id="22221"></span>
<div id="comment-22221" class="comment">
<div id="post-22221-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I already know how to render slippy maps. I have implemented it using MS4W. I just need to find a way to connect that map to Android when I connect using osmdroid.</p>
</div>
<div id="comment-22221-info" class="comment-info">
<span class="comment-age">(09 May '13, 15:14)</span> <span class="comment-user userinfo">Hishan</span>
</div>
</div>
<span id="22222"></span>
<div id="comment-22222" class="comment">
<div id="post-22222-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The tutorial suggests pointing MOBAC at a web site to create a zip file for use by the Osmdroid project. What goes wrong when you point MOBAC at your MS4W site? Or does that bit work and some other part of the tutorial fail?</p>
</div>
<div id="comment-22222-info" class="comment-info">
<span class="comment-age">(09 May '13, 15:24)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="22223"></span>
<div id="comment-22223" class="comment">
<div id="post-22223-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Why can't we just render the map tiles from web server without downloading and adding it to a zip file?</p>
</div>
<div id="comment-22223-info" class="comment-info">
<span class="comment-age">(09 May '13, 15:33)</span> <span class="comment-user userinfo">Hishan</span>
</div>
</div>
<span id="22225"></span>
<div id="comment-22225" class="comment not_top_scorer">
<div id="post-22225-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>The reason for downloading and storing in a zip file is so that users don't need to download the tiles over the air on demand at their mobile data tariff. If you want osmand to access a different online tile server (such as yours) that would work, but all your users would need access to your MS4W tile server all the time.</p>
<p>There's a bit of info in this thread: <a href="http://groups.google.com/group/osmdroid/browse_thread/thread/f27924c5df1cdc73">http://groups.google.com/group/osmdroid/browse_thread/thread/f27924c5df1cdc73</a></p>
<p>(in fact, if you want to ask about the specifics of Osmdroid you're more likely to get correct answers there rather than here)</p>
</div>
<div id="comment-22225-info" class="comment-info">
<span class="comment-age">(09 May '13, 15:48)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="22228"></span>
<div id="comment-22228" class="comment not_top_scorer">
<div id="post-22228-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Yes I want my app users to access the map online. Thank you for your help. But I am not using Osmand. The link you gave is a really good place to ask my questions. Thanks again.</p>
</div>
<div id="comment-22228-info" class="comment-info">
<span class="comment-age">(09 May '13, 16:08)</span> <span class="comment-user userinfo">Hishan</span>
</div>
</div>
<span id="22231"></span>
<div id="comment-22231" class="comment not_top_scorer">
<div id="post-22231-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Bah - sorry about that - me getting confused!</p>
<p>I've converted the "osmand" Google Groups link to the equivalent question in an "osmdroid" one.</p>
</div>
<div id="comment-22231-info" class="comment-info">
<span class="comment-age">(09 May '13, 16:14)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="22239"></span>
<div id="comment-22239" class="comment">
<div id="post-22239-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Thank you.</p>
</div>
<div id="comment-22239-info" class="comment-info">
<span class="comment-age">(09 May '13, 18:30)</span> <span class="comment-user userinfo">Hishan</span>
</div>
</div>
</div>
<div id="comment-tools-22216" class="comment-tools">
<span class="comments-showing"> showing 5 of 8 </span> <a href="#" class="show-all-comments-link">show 3 more comments</a>
</div>
<div class="clear">
&#10;</div>
<div id="comment-22216-form-container" class="comment-form-container">
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

