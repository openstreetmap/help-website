+++
type = "question"
title = "Setup tile server on RedHat"
description = '''Managed setting up a tile server on Ubuntu by following those instructions: https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/ However there is a requirement to create such tile server on RedHat instead. Using: Red Hat Enterprise Linux Server release 5.10 (Tikanga) Did anyone...'''
date = "2015-11-01T21:15:00Z"
lastmod = "2018-05-14T21:30:00Z"
weight = 46292
keywords = [ "tiles", "redhat", "tileserver" ]
aliases = [ "/questions/46292" ]
osqa_answers = 2
osqa_accepted = false
+++

<div class="headNormal">

# [Setup tile server on RedHat](/questions/46292/setup-tile-server-on-redhat)

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
<span id="post-46292-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46292-score" class="post-score" title="current number of votes">
1
</div>
<span id="post-46292-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Managed setting up a tile server on Ubuntu by following those instructions: <a href="https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/">https://switch2osm.org/serving-tiles/building-a-tile-server-from-packages/</a></p>
<p>However there is a requirement to create such tile server on RedHat instead. Using: Red Hat Enterprise Linux Server release 5.10 (Tikanga)</p>
<p>Did anyone try and succeeded in doing something similar?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-redhat" rel="tag" title="see questions tagged &#39;redhat&#39;">redhat</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>01 Nov '15, 21:15</strong></p>
<img src="https://secure.gravatar.com/avatar/dc42858283ab2bc1cdb1f5eda8bcad99?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="vvv13&#39;s gravatar image" />
<p><span>vvv13</span><br />
<span class="score" title="26 reputation points">26</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="2 badges"><span class="bronze">●</span><span class="badgecount">2</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="vvv13 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>01 Nov '15, 21:16</strong> </span></p>
</div>
</div>
<div id="comments-container-46292" class="comments-container">
<span id="46302"></span>
<div id="comment-46302" class="comment">
<div id="post-46302-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, welcome! Could you please clearly state a question and please keep <span>FAQ</span> in mind.</p>
</div>
<div id="comment-46302-info" class="comment-info">
<span class="comment-age">(02 Nov '15, 18:44)</span> <span class="comment-user userinfo">aseerel4c26 ♦</span>
</div>
</div>
<span id="46304"></span>
<div id="comment-46304" class="comment">
<div id="post-46304-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I don't believe you'll find similar packages for Redhat. Someone who tried building from source a couple of years ago hit a problem:</p>
<p><a href="/questions/16972/configure-linux-for-osm-tile-server/16994">https://help.openstreetmap.org/questions/16972/configure-linux-for-osm-tile-server/16994</a></p>
<p>I suspect that's a work-aroundable problem, and it'd be great if when you do work around it you stick an answer to the previous help question :)</p>
</div>
<div id="comment-46304-info" class="comment-info">
<span class="comment-age">(02 Nov '15, 18:57)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46292" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46292-form-container" class="comment-form-container">
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

<span id="46581"></span>

<div id="answer-container-46581" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46581-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46581-score" class="post-score" title="current number of votes">
3
</div>
<span id="post-46581-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Using RedHat 5 or CentOS 5 will be an interesting experience. Because the software that comes with the distribution is so ancient, you will have to build most software yourself. Assuming that you want to use a relatively recent style, you will need to compile this at a minimum</p>
<ul>
<li>GCC 4.8+ (C++11 support)</li>
<li>Autotools</li>
<li>boost</li>
<li>python</li>
<li>GEOS</li>
<li>PROJ.4</li>
<li>PostgreSQL (9.1+)</li>
<li>PostGIS (2.0+)</li>
<li>osm2pgsql</li>
<li>libicuuc</li>
<li>libfreetype</li>
<li>libharfbuzz</li>
<li>libfreetype (thanks to a bootstrapping issue with harfbuzz)</li>
<li>Mapnik</li>
<li>Renderd</li>
<li>nodejs</li>
<li>npm</li>
<li>Apache</li>
</ul>
<p>This list is certainly not complete. There are no guides that will spell out what you need to do. You might find RPMs for <strong>some</strong> of this software from other RPM sources.</p>
<p>Expect to encounter issues that no one else has, and expect to have to solve them yourself. I've run tile servers on CentOS 6 and it was difficult enough.</p>
<p>You might be able to pay a consultant to do this, but they'd charge hourly since it'd take an unknown amount of time.</p>
<p>Unless you have <strong>significant</strong> RedHat experience within your organization, don't try this. Use RedHat/CentOS 7 or another distribution.</p>
<p>An alternative would be to try to use really old versions of everything. This probably isn't easier, and would get you a tile server that can't run modern styles (or import recent OSM data, thanks to 32-bit limits!).</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>14 Nov '15, 01:19</strong></p>
<img src="https://secure.gravatar.com/avatar/5634c46072077e10f5b7c0da9b4bbb62?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="pnorman&#39;s gravatar image" />
<p><span>pnorman</span><br />
<span class="score" title="2352 reputation points"><span>2.4k</span></span><span title="5 badges"><span class="badge1">●</span><span class="badgecount">5</span></span><span title="21 badges"><span class="silver">●</span><span class="badgecount">21</span></span><span title="40 badges"><span class="bronze">●</span><span class="badgecount">40</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="pnorman has 9 accepted answers">18%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>14 Nov '15, 01:21</strong> </span></p>
</div>
</div>
<div id="comments-container-46581" class="comments-container">
&#10;</div>
<div id="comment-tools-46581" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46581-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

<span id="46580"></span>

<div id="answer-container-46580" class="answer">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-46580-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46580-score" class="post-score" title="current number of votes">
2
</div>
<span id="post-46580-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>Setting up a tile server on RedHat is definitely possible, I have done it many times. It might require compiling some resources from scratch because there's no ready-made packages; sometimes you can just get a Fedora SRPM and rpmbuild --rebuild that or so.</p>
<p>I hope you don't expect a 10-page setup tutorial in response to your question but if you get stuck on something particular, feel free to place a precise question on this forum.</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>13 Nov '15, 23:30</strong></p>
<img src="https://secure.gravatar.com/avatar/a2b38d937e70ab39d895d17da0dd1ba4?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Frederik%20Ramm&#39;s gravatar image" />
<p><span>Frederik Ramm ♦</span><br />
<span class="score" title="82494 reputation points"><span>82.5k</span></span><span title="92 badges"><span class="badge1">●</span><span class="badgecount">92</span></span><span title="720 badges"><span class="silver">●</span><span class="badgecount">720</span></span><span title="1273 badges"><span class="bronze">●</span><span class="badgecount">1273</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Frederik Ramm has 417 accepted answers">23%</span></p>
</div>
</div>
<div id="comments-container-46580" class="comments-container">
<span id="48047"></span>
<div id="comment-48047" class="comment">
<div id="post-48047-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/104/frederik-ramm">@Frederik Ramm</a>, It would be very helpful if you provide any series of steps to achive tile server installation in rhel.</p>
</div>
<div id="comment-48047-info" class="comment-info">
<span class="comment-age">(11 Feb '16, 06:57)</span> <span class="comment-user userinfo">Naren970</span>
</div>
</div>
<span id="48048"></span>
<div id="comment-48048" class="comment">
<div id="post-48048-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>Afraid I might have overlooked the version number 5 requirement in your message; I certainly never installed a tile server on RHEL5. You will likely not be able to set up a <em>modern</em> tile server on this system; I think your best bet might be to get hold of the 0.7 version of Mapnik and start with compiling that, resolving all the dependencies like boost etc.; once you've managed that, renderd and mod_tile should be relatively easy. Then you'll want to get an older version of osm2pgsql and an older version of the OSM map style (not openstreetmap-carto but from when it still was an XML style), that will work with Mapnik 0.7.</p>
</div>
<div id="comment-48048-info" class="comment-info">
<span class="comment-age">(11 Feb '16, 08:42)</span> <span class="comment-user userinfo">Frederik Ramm ♦</span>
</div>
</div>
<span id="63468"></span>
<div id="comment-63468" class="comment">
<div id="post-63468-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Hi, Really interesting that there is no even one good instruction to Setup openstreetmap on Redhat.</p>
</div>
<div id="comment-63468-info" class="comment-info">
<span class="comment-age">(14 May '18, 15:38)</span> <span class="comment-user userinfo">ArashArteman</span>
</div>
</div>
<span id="63474"></span>
<div id="comment-63474" class="comment">
<div id="post-63474-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Please don't post answers like this. This belongs in the comments section. Try docker first and then post your results.</p>
</div>
<div id="comment-63474-info" class="comment-info">
<span class="comment-age">(14 May '18, 16:38)</span> <span class="comment-user userinfo">gfitz</span>
</div>
</div>
<span id="63480"></span>
<div id="comment-63480" class="comment">
<div id="post-63480-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="https://help.openstreetmap.org/users/14985/gfitz">@gfitz</a>: I converted <a href="https://help.openstreetmap.org/users/15118/arasharteman">@ArashArteman</a>'s 'answer' to a comment.</p>
</div>
<div id="comment-63480-info" class="comment-info">
<span class="comment-age">(14 May '18, 21:30)</span> <span class="comment-user userinfo">SK53 ♦</span>
</div>
</div>
</div>
<div id="comment-tools-46580" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46580-form-container" class="comment-form-container">
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

