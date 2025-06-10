+++
type = "question"
title = "Error while installing Overpass API on Ubuntu 16.04"
description = '''Hi, someone can help me? I can&#x27;t install OSM :~$ lsb_release -a Distributor ID: Ubuntu Description: Ubuntu 16.04.1 LTS Release: 16.04 Codename: xenial   cd /mnt/data/ sudo mkdir openstreetmap sudo apt-get update sudo apt-get upgrade sudo apt-get autoremove sudo apt-get install g++ make expat libexpa...'''
date = "2016-08-11T19:00:00Z"
lastmod = "2016-08-12T16:39:00Z"
weight = 51355
keywords = [ "overpassapi", "installation", "ubuntu" ]
aliases = [ "/questions/51355" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Error while installing Overpass API on Ubuntu 16.04](/questions/51355/error-while-installing-overpass-api-on-ubuntu-1604)

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
<span id="post-51355-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-51355-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-51355-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hi, someone can help me? I can't install OSM</p>
<pre><code>:~$ lsb_release -a
Distributor ID: Ubuntu
Description:    Ubuntu 16.04.1 LTS
Release:    16.04
Codename:   xenial</code></pre>
<pre><code>cd /mnt/data/
sudo mkdir openstreetmap
sudo apt-get update
sudo apt-get upgrade
sudo apt-get autoremove
sudo apt-get install g++ make expat libexpat1-dev zlib1g-dev
cd /mnt/data/openstreetmap
wget http://dev.overpass-api.de/releases/osm-3s_v0.7.52.tar.gz
tar xvfz osm-3s_v*.tar.gz
export EXEC_DIR=/mnt/data/openstreetmap/osm-3s_v0.7.52
mkdir db
export DB_DIR=/mnt/data/openstreetmap/db
export PLANET_FILE=/mnt/data/openstreetmap/planet_file
mkdir replicate
export REPLICATE_DIR=/mnt/data/openstreetmap/replicate
cd osm-3s_v*
./configure CXXFLAGS=&quot;-O3&quot; --prefix=$EXEC_DIR
make
make install
....
.....
....
&#10;Makefile:1101: fallo en las instrucciones para el objetivo &#39;install-dist_testbinSCRIPTS&#39;
make[2]: *** [install-dist_testbinSCRIPTS] Error 1
make[2]: se sale del directorio &#39;/mnt/data/openstreetmap/osm-3s_v0.7.52/test-bin&#39;
Makefile:1350: fallo en las instrucciones para el objetivo &#39;install-am&#39;
make[1]: *** [install-am] Error 2
make[1]: se sale del directorio &#39;/mnt/data/openstreetmap/osm-3s_v0.7.52/test-bin&#39;
Makefile:1496: fallo en las instrucciones para el objetivo &#39;install-recursive&#39;
make: *** [install-recursive] Error 1</code></pre>
<p>Thanks in advance</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpassapi" rel="tag" title="see questions tagged &#39;overpassapi&#39;">overpassapi</span> <span class="post-tag tag-link-installation" rel="tag" title="see questions tagged &#39;installation&#39;">installation</span> <span class="post-tag tag-link-ubuntu" rel="tag" title="see questions tagged &#39;ubuntu&#39;">ubuntu</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>11 Aug '16, 19:00</strong></p>
<img src="https://secure.gravatar.com/avatar/304bf9b97689c5eb6191600403aaf65b?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="arcadio%20ortega&#39;s gravatar image" />
<p><span>arcadio ortega</span><br />
<span class="score" title="41 reputation points">41</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="arcadio ortega has no accepted answers">0%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>11 Aug '16, 21:05</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/52d3234f3be58156770e8a91d575bfbd?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="scai&#39;s gravatar image" />
<p><span>scai ♦</span><br />
<span class="score" title="33317 reputation points"><span>33.3k</span></span><span title="21 badges"><span class="badge1">●</span><span class="badgecount">21</span></span><span title="309 badges"><span class="silver">●</span><span class="badgecount">309</span></span><span title="459 badges"><span class="bronze">●</span><span class="badgecount">459</span></span></p>
</div>
</div>
<div id="comments-container-51355" class="comments-container">
<span id="51356"></span>
<div id="comment-51356" class="comment">
<div id="post-51356-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Can you provide English messages and the <em>full</em> output of the failing command?</p>
</div>
<div id="comment-51356-info" class="comment-info">
<span class="comment-age">(11 Aug '16, 19:11)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="51358"></span>
<div id="comment-51358" class="comment">
<div id="post-51358-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>Your title is quite misleading. Can you change it to Overpass API, assuming that's what you were planning to install when talking about "installing OSM"?</p>
<p>Also I don't recommend running plain 0.7.52 due to some 64bit issue. If you're not comfortable patching the sources yourself or running a pre-release version, you need to wait for the next release. There's no other workaround available at this time.</p>
</div>
<div id="comment-51358-info" class="comment-info">
<span class="comment-age">(11 Aug '16, 20:54)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="51363"></span>
<div id="comment-51363" class="comment">
<div id="post-51363-score" class="comment-score">
1
</div>
<div class="comment-text">
<p><a href="http://help.openstreetmap.org/users/8708/mmd">@mmd</a> I've changed title and tags.</p>
</div>
<div id="comment-51363-info" class="comment-info">
<span class="comment-age">(12 Aug '16, 08:35)</span> <span class="comment-user userinfo">scai ♦</span>
</div>
</div>
<span id="51374"></span>
<div id="comment-51374" class="comment">
<div id="post-51374-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I tried on i386 and amd64 with the same result. Yes I managed to install the osm-3s_v0.7.4.tar.gz release. I think the problem is osm-3s_v0.7.52.tar.gz with 16.04. I will wait for a new release. Thanks</p>
</div>
<div id="comment-51374-info" class="comment-info">
<span class="comment-age">(12 Aug '16, 16:39)</span> <span class="comment-user userinfo">arcadio ortega</span>
</div>
</div>
</div>
<div id="comment-tools-51355" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-51355-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

