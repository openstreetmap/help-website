+++
type = "question"
title = "The renderd_expire command update wrong tiles."
description = '''I make an edit on a place which can be see on the picture1, i create a test area called iD_test20170104.1 as show on the picture2, but a way occured which point to the place which i built before, then i delete the iD_test20170104.1, but the way still exist. And now i do not know how to restore the m...'''
date = "2017-01-04T06:05:00Z"
lastmod = "2017-01-10T11:19:00Z"
weight = 53854
keywords = [ "tiles", "renderd", "editor", "tileserver" ]
aliases = [ "/questions/53854" ]
osqa_answers = 1
osqa_accepted = false
+++

<div class="headNormal">

# [The renderd_expire command update wrong tiles.](/questions/53854/the-renderd_expire-command-update-wrong-tiles)

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
<span id="post-53854-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53854-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53854-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>I make an edit on a place which can be see on the picture1, i create a test area called iD_test20170104.1 as show on the picture2, but a way occured which point to the place which i built before, then i delete the iD_test20170104.1, but the way still exist. And now i do not know how to restore the map to the original state.</p>
<p>It is on my own rails port, and i use iD editor to make the edit, and use osmosis command to produce a changes.osc.gz file, then use osm2pgsql with -append and -e options to generate a expire.list file, finally, i use "cat /data/mod_map/expire.list | /root/src/mod_tile/render_expired -m osmcarto -z 10 -Z 18 -T=10" command to re-renderd the tile, but the error occurs.</p>
<p>Is there a possibility that the changes.osc.gz files node id have conflict with the exist nodes causes the error? The changes.osc.gz file can be shown below.</p>
<pre><code>&lt;?xml version=&#39;1.0&#39; encoding=&#39;UTF-8&#39;?&gt;
&lt;osmChange version=&quot;0.6&quot; generator=&quot;Osmosis 0.45&quot;&gt;
  &lt;create&gt;
    &lt;node id=&quot;12&quot; version=&quot;1&quot; timestamp=&quot;2017-01-04T01:56:57Z&quot; uid=&quot;2&quot; user=&quot;osm_test&quot; changeset=&quot;4&quot; lat=&quot;39.9760643&quot; lon=&quot;116.3371492&quot;/&gt;
     &lt;node id=&quot;13&quot; version=&quot;1&quot; timestamp=&quot;2017-01-04T01:56:57Z&quot; uid=&quot;2&quot; user=&quot;osm_test&quot; changeset=&quot;4&quot; lat=&quot;39.9761444&quot; lon=&quot;116.337109&quot;/&gt;
    &lt;node id=&quot;14&quot; version=&quot;1&quot; timestamp=&quot;2017-01-04T01:56:57Z&quot; uid=&quot;2&quot; user=&quot;osm_test&quot; changeset=&quot;4&quot; lat=&quot;39.9762369&quot; lon=&quot;116.3371439&quot;/&gt;
    &lt;node id=&quot;15&quot; version=&quot;1&quot; timestamp=&quot;2017-01-04T01:56:57Z&quot; uid=&quot;2&quot; user=&quot;osm_test&quot; changeset=&quot;4&quot; lat=&quot;39.9762369&quot; lon=&quot;116.3372592&quot;/&gt;
    &lt;node id=&quot;16&quot; version=&quot;1&quot; timestamp=&quot;2017-01-04T01:56:57Z&quot; uid=&quot;2&quot; user=&quot;osm_test&quot; changeset=&quot;4&quot; lat=&quot;39.9761814&quot; lon=&quot;116.3373584&quot;/&gt;
    &lt;node id=&quot;17&quot; version=&quot;1&quot; timestamp=&quot;2017-01-04T01:56:57Z&quot; uid=&quot;2&quot; user=&quot;osm_test&quot; changeset=&quot;4&quot; lat=&quot;39.9761198&quot; lon=&quot;116.3373745&quot;/&gt;
    &lt;node id=&quot;18&quot; version=&quot;1&quot; timestamp=&quot;2017-01-04T01:56:57Z&quot; uid=&quot;2&quot; user=&quot;osm_test&quot; changeset=&quot;4&quot; lat=&quot;39.976056&quot; lon=&quot;116.337337&quot;/&gt;
    &lt;node id=&quot;19&quot; version=&quot;1&quot; timestamp=&quot;2017-01-04T01:56:57Z&quot; uid=&quot;2&quot; user=&quot;osm_test&quot; changeset=&quot;4&quot; lat=&quot;39.9760314&quot; lon=&quot;116.3372377&quot;/&gt;
    &lt;way id=&quot;2&quot; version=&quot;1&quot; timestamp=&quot;2017-01-04T01:56:57Z&quot; uid=&quot;2&quot; user=&quot;osm_test&quot; changeset=&quot;4&quot;&gt;
      &lt;nd ref=&quot;12&quot;/&gt;
      &lt;nd ref=&quot;13&quot;/&gt;
      &lt;nd ref=&quot;14&quot;/&gt;
      &lt;nd ref=&quot;15&quot;/&gt;
      &lt;nd ref=&quot;16&quot;/&gt;
      &lt;nd ref=&quot;17&quot;/&gt;
      &lt;nd ref=&quot;18&quot;/&gt;
      &lt;nd ref=&quot;19&quot;/&gt;
      &lt;nd ref=&quot;12&quot;/&gt;
      &lt;tag k=&quot;description&quot; v=&quot;2017.1.4日9:57在大运村的一个测试区域&quot;/&gt;
      &lt;tag k=&quot;leisure&quot; v=&quot;park&quot;/&gt;
      &lt;tag k=&quot;name&quot; v=&quot;iD_test20170104.1&quot;/&gt;
    &lt;/way&gt;
  &lt;/create&gt;
&lt;/osmChange&gt;</code></pre>
<p><img src="/upfiles/1_6mt7z3j.png" alt="alt text" /></p>
<p><img src="/upfiles/2_1kYH4It.png" alt="alt text" /></p>
<p><img src="/upfiles/3_GyHf7qe.png" alt="alt text" /></p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-tiles" rel="tag" title="see questions tagged &#39;tiles&#39;">tiles</span> <span class="post-tag tag-link-renderd" rel="tag" title="see questions tagged &#39;renderd&#39;">renderd</span> <span class="post-tag tag-link-editor" rel="tag" title="see questions tagged &#39;editor&#39;">editor</span> <span class="post-tag tag-link-tileserver" rel="tag" title="see questions tagged &#39;tileserver&#39;">tileserver</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>04 Jan '17, 06:05</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</img>
</div>
<div class="post-update-info post-update-info-edited">
<p><span> edited <strong>10 Jan '17, 10:13</strong> </span></p>
<img src="https://secure.gravatar.com/avatar/0bf1aa22f7f5e045b0eb8beb79fe7907?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="SomeoneElse&#39;s gravatar image" />
<p><span>SomeoneElse ♦</span><br />
<span class="score" title="36866 reputation points"><span>36.9k</span></span><span title="71 badges"><span class="badge1">●</span><span class="badgecount">71</span></span><span title="370 badges"><span class="silver">●</span><span class="badgecount">370</span></span><span title="866 badges"><span class="bronze">●</span><span class="badgecount">866</span></span></p>
</img>
</div>
</div>
<div id="comments-container-53854" class="comments-container">
<span id="53895"></span>
<div id="comment-53895" class="comment">
<div id="post-53895-score" class="comment-score">
1
</div>
<div class="comment-text">
<p>Also is this on osm.org or on your own copy of the rails port (with data loaded)?</p>
</div>
<div id="comment-53895-info" class="comment-info">
<span class="comment-age">(06 Jan '17, 13:22)</span> <span class="comment-user userinfo">SomeoneElse ♦</span>
</div>
</div>
<span id="53900"></span>
<div id="comment-53900" class="comment">
<div id="post-53900-score" class="comment-score">
2
</div>
<div class="comment-text">
<p>It is on my own rails port, and i use iD editor to make the edit, and use osmosis command to produce a changes.osc.gz file, then use osm2pgsql with -append and -e options to generate a expire.list file, finally, i use "cat /data/mod_map/expire.list | /root/src/mod_tile/render_expired -m osmcarto -z 10 -Z 18 -T=10" command to re-renderd the tile, but the error occurs.</p>
</div>
<div id="comment-53900-info" class="comment-info">
<span class="comment-age">(07 Jan '17, 08:02)</span> <span class="comment-user userinfo">yuyy</span>
</div>
</div>
</div>
<div id="comment-tools-53854" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53854-form-container" class="comment-form-container">
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

<span id="53967"></span>

<div id="answer-container-53967" class="answer answered-by-owner">

<table style="width:100%;">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr>
<td style="width: 30px; vertical-align: top"><div class="vote-buttons">
<span id="post-53967-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-53967-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-53967-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span>
</div></td>
<td><div class="item-right">
<div class="answer-body">
<p>I think it was caused by the conflict id in the changes.osc.gz file and the tile server database. I installed my own rails port, and when i use the editor to make a changes file, the index id of the node and way are begin at 1, but there has be a node or a way which id is 1 in the tile server database, so when i use osm2pgsql with -append option to import the changes file into the database, the error occurs.</p>
<p>And now, what confuses me is that the index id of the nodes and ways are automatically generated by the osmosis command, how can i set them to start at a large index number?</p>
</div>
<div class="answer-controls post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>answered <strong>10 Jan '17, 11:19</strong></p>
<img src="https://secure.gravatar.com/avatar/3522efac952d508cf251cd2590e68ca5?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="yuyy&#39;s gravatar image" />
<p><span>yuyy</span><br />
<span class="score" title="236 reputation points">236</span><span title="22 badges"><span class="badge1">●</span><span class="badgecount">22</span></span><span title="24 badges"><span class="silver">●</span><span class="badgecount">24</span></span><span title="31 badges"><span class="bronze">●</span><span class="badgecount">31</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="yuyy has one accepted answer">20%</span></p>
</img>
</div>
</div>
<div id="comments-container-53967" class="comments-container">
&#10;</div>
<div id="comment-tools-53967" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-53967-form-container" class="comment-form-container">
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

