+++
type = "question"
title = "mod_tile build on RHEL5"
description = '''I am trying to build mod_tile on my RHEL5 Tile Server. Attempting to modify these instructions: http://en.flossmanuals.net/openstreetmap/setting-up-your-own-tile-server/ for RHEL5, and installing Mapnik from these instructions: http://svn.osgeo.org/osgeo/foss4g/benchmarking/wms/2010/mapnik/scripts/i...'''
date = "2013-02-25T22:11:00Z"
lastmod = "2013-02-25T22:11:00Z"
weight = 20286
keywords = [ "mod_tile", "mapnik", "tileserver" ]
aliases = [ "/questions/20286" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [mod_tile build on RHEL5](/questions/20286/mod_tile-build-on-rhel5)

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
<span id="post-20286-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-20286-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-20286-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I am trying to build mod_tile on my RHEL5 Tile Server. Attempting to modify these instructions: <a href="http://en.flossmanuals.net/openstreetmap/setting-up-your-own-tile-server/">http://en.flossmanuals.net/openstreetmap/setting-up-your-own-tile-server/</a> for RHEL5, and installing Mapnik from these instructions: <a href="http://svn.osgeo.org/osgeo/foss4g/benchmarking/wms/2010/mapnik/scripts/install_mapnik_rhel_5.5.sh">http://svn.osgeo.org/osgeo/foss4g/benchmarking/wms/2010/mapnik/scripts/install_mapnik_rhel_5.5.sh</a> I finally have created a static image with mapnik0.7.3. However now I am trying to build mod_tile, with:</p>
<p>./autogen.sh \ --with-libmapnik=/opt/mapnik/mapnik-seven/lib64 \ --with-boost=no \ --with-apxs=/opt/mapnik/bin/apxs \ --with-boost-libdir=/opt/mapnik/lib</p>
<p>./configure \ --with-libmapnik=/opt/mapnik/mapnik-seven/lib64 \ --with-boost=no \ --with-apxs=/opt/mapnik/bin/apxs \ --with-boost-libdir=/opt/mapnik/lib</p>
<p>Now when I issue 'make' I get this mess:</p>
<p>make all-recursive make[1]: Entering directory <code>/opt/mapnik/src/mod_tile' Making all in iniparser3.0b make[2]: Entering directory</code>/opt/mapnik/src/mod_tile/iniparser3.0b' if --tag=CC --mode=compile gcc -std=gnu99 -DHAVE_CONFIG_H -I. -I. -I.. -O3 -MT iniparser.lo -MD -MP -MF ".deps/iniparser.Tpo" -c -o iniparser.lo <code>test -f 'src/iniparser.c' || echo './'</code>src/iniparser.c; \ then mv -f ".deps/iniparser.Tpo" ".deps/iniparser.Plo"; else rm -f ".deps/iniparser.Tpo"; exit 1; fi /bin/sh: --tag=CC: command not found make[2]: <strong><em>[iniparser.lo] Error 1 make[2]: Leaving directory <code>/opt/mapnik/src/mod_tile/iniparser3.0b' make[1]: *** [all-recursive] Error 1 make[1]: Leaving directory</code>/opt/mapnik/src/mod_tile' make:</em></strong> [all] Error 2</p>
<p>I am at my wit's end. I am a linux newbie so don't assume I know or did anything ;-)</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-mod_tile" rel="tag" title="see questions tagged &#39;mod_tile&#39;">mod_tile</span> <span class="post-tag tag-link-mapnik" rel="tag" title="see questions tagged &#39;mapnik&#39;">mapnik</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>25 Feb '13, 22:11</strong></p>
<img src="https://secure.gravatar.com/avatar/fbb15843641ffaf1c2259cc7ebb4735c?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="maw269&#39;s gravatar image" />
<p><span>maw269</span><br />
<span class="score" title="115 reputation points">115</span><span title="7 badges"><span class="badge1">●</span><span class="badgecount">7</span></span><span title="7 badges"><span class="silver">●</span><span class="badgecount">7</span></span><span title="14 badges"><span class="bronze">●</span><span class="badgecount">14</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="maw269 has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>25 Feb '13, 22:12</strong> </span></p>
</div>
</div>
<div id="comments-container-20286" class="comments-container">
&#10;</div>
<div id="comment-tools-20286" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-20286-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

