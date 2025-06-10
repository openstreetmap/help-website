+++
type = "question"
title = "[closed] Why can&#x27;t i import my osmfiltered file into an overpass server?"
description = '''Hello everyone.  For an application of mine I am trying to set up my own Overpass Api server. Importing andorra-latest.osm.bz2 with the following command works fine, beside ~a dozen ways that are referenced in relations can&#x27;t be found, which is probably due to it being an extracted file and not the ...'''
date = "2015-11-04T16:30:00Z"
lastmod = "2015-11-04T17:55:00Z"
weight = 46389
keywords = [ "overpass", "osmfilter" ]
aliases = [ "/questions/46389" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [\[closed\] Why can't i import my osmfiltered file into an overpass server?](/questions/46389/why-cant-i-import-my-osmfiltered-file-into-an-overpass-server)

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
<span id="post-46389-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-46389-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-46389-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone.</p>
<p>For an application of mine I am trying to set up my own Overpass Api server. Importing <a href="http://download.geofabrik.de/europe/andorra-latest.osm.bz2">andorra-latest.osm.bz2</a> with the following command works fine, beside ~a dozen ways that are referenced in relations can't be found, which is probably due to it being an extracted file and not the planet.osm file.</p>
<pre><code>nohup ./srv/osm3s/bin/init_osm3s.sh /root/andorra-latest.osm.bz2 /srv/osm3sdb /srv/osm3s</code></pre>
<p>In hope of saving some space on the hard disk i created a file that contains only the data that are necessary for my application, using osmfilter. The command i used:</p>
<pre><code>osmfilter D:\osm\germany-latest.osm --keep= --keep-ways=&quot;water= or waterway= or natural= or leisure= or landuse= or landcover=&quot; --keep-relations=&quot;water= or natural= or leisure= or landuse= or landcover= or waterway=&quot; -o=D:\osm\germany-filtered.osm</code></pre>
<p>Which reduced the file size down to about 20%. Afterwards i put it into a bz2 archiv using 7z.</p>
<p>using the same command that worked for andorra, i get the following error:</p>
<pre><code>Reading XML file ...terminate called after throwing an instance of &#39;std::bad_alloc&#39;
  what():  std::bad_alloc
./srv/osm3s/bin/init_osm3s.sh: line 44: 15227 Broken pipe             bunzip2 &lt; $PLANET_FILE
 15228 Aborted                 (core dumped) | $EXEC_DIR/bin/update_database --db-dir=$DB_DIR/ $META $COMPRESSION</code></pre>
<p>does anyone have an idea how to solve this? Is it even possible to import osmfiltered files?</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-osmfilter" rel="tag" title="see questions tagged &#39;osmfilter&#39;">osmfilter</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Nov '15, 16:30</strong></p>
<img src="https://secure.gravatar.com/avatar/991a1daf7de47d3dcc3d94933c70ce2d?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="EinFreierNick&#39;s gravatar image" />
<p><span>EinFreierNick</span><br />
<span class="score" title="121 reputation points">121</span><span title="4 badges"><span class="badge1">●</span><span class="badgecount">4</span></span><span title="5 badges"><span class="silver">●</span><span class="badgecount">5</span></span><span title="12 badges"><span class="bronze">●</span><span class="badgecount">12</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="EinFreierNick has one accepted answer">50%</span></p>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> closed <strong>04 Nov '15, 17:56</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/264d84ab05b942224b05960903eba7a7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="mmd&#39;s gravatar image" />
<p><span>mmd</span><br />
<span class="score" title="5682 reputation points"><span>5.7k</span></span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="53 badges"><span class="silver">●</span><span class="badgecount">53</span></span><span title="88 badges"><span class="bronze">●</span><span class="badgecount">88</span></span></p>
</div>
</div>
<div id="comments-container-46389" class="comments-container">
<span id="46390"></span>
<div id="comment-46390" class="comment">
<div id="post-46390-score" class="comment-score">
&#10;</div>
<div class="comment-text">
<p>I would recommend to post this question on the Overpass API developer mailing list, as it is too specific for Help OSM and unlikely to help a lot of other users.</p>
<p>Link: <a href="http://listes.openstreetmap.fr/wws/info/overpass">http://listes.openstreetmap.fr/wws/info/overpass</a> -&gt; also mirrored on gmane.org and nabble.com, both of which offer a web frontend. Btw: don't forget to include the Overpass APi version you're using and some specs about your system. Your error message may be related to a lack of available memory.</p>
</div>
<div id="comment-46390-info" class="comment-info">
<span class="comment-age">(04 Nov '15, 16:45)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
<span id="46391"></span>
<div id="comment-46391" class="comment">
<div id="post-46391-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Follow up is <a href="http://permalink.gmane.org/gmane.comp.gis.openstreetmap.overpass/174">here</a>.</p>
</div>
<div id="comment-46391-info" class="comment-info">
<span class="comment-age">(04 Nov '15, 17:55)</span> <span class="comment-user userinfo">mmd</span>
</div>
</div>
</div>
<div id="comment-tools-46389" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-46389-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

<div class="question-status" style="margin-bottom:15px">

### The question has been closed for the following reason "Follow up on Overpass dev list" by mmd 04 Nov '15, 17:56

</div>

</div>

</div>

