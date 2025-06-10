+++
type = "question"
title = "Overpass: Limited area database (extract) create area infinite loop alternative?"
description = '''Hello everyone; I have initialed overpass database from an extract for the state of Arizona, USA. I replaced &quot;rules_loop.sh&quot; script shipped with source with the following script: #!/usr/bin/bash  DB_DIR=/mnt/nvme4/op2-meta EXEC_DIR=/usr/local/bin RULES_DIR=/usr/local/rules LOG_FILE=$DB_DIR/logs/op_u...'''
date = "2022-05-08T12:44:00Z"
lastmod = "2022-05-08T12:44:00Z"
weight = 84407
keywords = [ "initialize", "overpass", "database" ]
aliases = [ "/questions/84407" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [Overpass: Limited area database (extract) create area infinite loop alternative?](/questions/84407/overpass-limited-area-database-extract-create-area-infinite-loop-alternative)

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
<span id="post-84407-upvote" class="ajax-command post-vote up" rel="nofollow" title="I like this post (click again to cancel)"> </span>
<div id="post-84407-score" class="post-score" title="current number of votes">
0
</div>
<span id="post-84407-downvote" class="ajax-command post-vote down" rel="nofollow" title="I dont like this post (click again to cancel)"> </span> <span id="favorite-mark" class="ajax-command favorite-mark" rel="nofollow" title="mark/unmark this question as favorite (click again to cancel)"> </span>
<div id="favorite-count" class="favorite-count">
&#10;</div>
</div></td>
<td><div id="item-right">
<div class="question-body">
<p>Hello everyone;</p>
<p>I have initialed overpass database from an extract for the state of Arizona, USA. I replaced "rules_loop.sh" script shipped with source with the following script:</p>
<pre><code>#!/usr/bin/bash
&#10;DB_DIR=/mnt/nvme4/op2-meta
EXEC_DIR=/usr/local/bin
RULES_DIR=/usr/local/rules
LOG_FILE=$DB_DIR/logs/op_update_area.log
&#10;while [[ true ]]; do
{
  echo &quot;`date &#39;+%F %T&#39;`: update started&quot; &gt;&gt;$LOG_FILE
  #  ./osm3s_query --progress --rules &lt;$DB_DIR/rules/areas.osm3s
  ionice -c 2 -n 7 nice -n 19 $EXEC_DIR/osm3s_query --progress --rules &lt;$RULES_DIR/areas.osm3s
  echo &quot;`date &#39;+%F %T&#39;`: update finished&quot; &gt;&gt;$LOG_FILE
  sleep 3
}; done</code></pre>
<p>Do I need this infinite loop for this small area extract? Is there any alternative?</p>
<p>Thank you all</p>
<p>Wael Hammoudeh</p>
</div>
<div id="question-tags" class="tags-container tags">
<span class="post-tag tag-link-initialize" rel="tag" title="see questions tagged &#39;initialize&#39;">initialize</span> <span class="post-tag tag-link-overpass" rel="tag" title="see questions tagged &#39;overpass&#39;">overpass</span> <span class="post-tag tag-link-database" rel="tag" title="see questions tagged &#39;database&#39;">database</span>
</div>
<div id="question-controls" class="post-controls">
&#10;</div>
<div class="post-update-info-container">
<div class="post-update-info post-update-info-user">
<p>asked <strong>08 May '22, 12:44</strong></p>
<img src="https://secure.gravatar.com/avatar/88d38e1916b4f2210db71007b0b36b8e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Wael&#39;s gravatar image" />
<p><span>Wael</span><br />
<span class="score" title="11 reputation points">11</span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="3 badges"><span class="silver">●</span><span class="badgecount">3</span></span><span title="6 badges"><span class="bronze">●</span><span class="badgecount">6</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Wael has no accepted answers">0%</span></p>
</div>
</div>
<div id="comments-container-84407" class="comments-container">
&#10;</div>
<div id="comment-tools-84407" class="comment-tools">
&#10;</div>
<div class="clear">
&#10;</div>
<div id="comment-84407-form-container" class="comment-form-container">
&#10;</div>
<div class="clear">
&#10;</div>
</div></td>
</tr>
</tbody>
</table>

</div>

</div>

