+++
type = "question"
title = "How to rewrite io_stat.c"
description = '''Hello, i need to rewrite code io_stat.c to get in io_graph to get 2 more values (0,0001 and 0,00001). I try but i get values 5 sec and 0,3 sec ... can someone help? Here my rewrite file : http://www.sendspace.com/file/2dz8yc'''
date = "2013-12-04T11:53:00Z"
lastmod = "2013-12-04T11:53:00Z"
weight = 27772
keywords = [ "io_stat.c", "rewrite" ]
aliases = [ "/questions/27772" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [How to rewrite io\_stat.c](/questions/27772/how-to-rewrite-io_statc)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-27772-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello, i need to rewrite code io_stat.c to get in io_graph to get 2 more values (0,0001 and 0,00001). I try but i get values 5 sec and 0,3 sec ... can someone help? Here my rewrite file : <a href="http://www.sendspace.com/file/2dz8yc">http://www.sendspace.com/file/2dz8yc</a></p></div><div id="question-tags" class="tags-container tags">io_stat.c rewrite</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>04 Dec '13, 11:53</strong></p><img src="https://secure.gravatar.com/avatar/efa790b8f1a2853b5af7ec8f5646b274?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Yszty&#39;s gravatar image" /><p>Yszty<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Yszty has no accepted answers">0%</span></p></div></div><div id="comments-container-27772" class="comments-container"><span id="27969"></span><div id="comment-27969" class="comment"><div id="post-27969-score" class="comment-score"></div><div class="comment-text"><p>I will try again. I need additional values of Tick interval in IO Graph. I need 100us, 10us and 1 us (microseconds). I have changed io_stat.c source code. In io_stat.c I change:</p><pre><code>static const guint tick_interval_values[MAX_TICK_VALUES] = { 1, 10, 100, 1000, 10000, 100000, 1000000, 6000000, 60000000 };</code></pre><p>and</p><pre><code>if (tick_interval_values[i] &gt;= 6000000) {
        g_snprintf(str, sizeof(str), &quot;%u min&quot;, tick_interval_values[i]/6000000);
    } else if (tick_interval_values[i] &gt;= 10000000) {
        g_snprintf(str, sizeof(str), &quot;%u sec&quot;, tick_interval_values[i]/100000);
    } else if (tick_interval_values[i] &gt;= 100000) {
        g_snprintf(str, sizeof(str), &quot;%u sec&quot;, tick_interval_values[i]/100000);
    } else if (tick_interval_values[i] &gt;= 10000) {
        g_snprintf(str, sizeof(str), &quot;0.%1u sec&quot;, (tick_interval_values[i]/10000)%10);
    } else if (tick_interval_values[i] &gt;= 1000) {
        g_snprintf(str, sizeof(str), &quot;0.%02u sec&quot;, (tick_interval_values[i]/1000)%10);
    } else if (tick_interval_values[i] &gt;= 100) {
        g_snprintf(str, sizeof(str), &quot;0.%03u sec&quot;, (tick_interval_values[i]/100)%10);
    } else if (tick_interval_values[i] &gt;= 10) {
        g_snprintf(str, sizeof(str), &quot;0.%04u sec&quot;, (tick_interval_values[i]/10)%10);
    } else if (tick_interval_values[i] &gt;= 1) {
        g_snprintf(str, sizeof(str), &quot;0.%05u sec&quot;, (tick_interval_values[i])%10);
    } else {
        g_snprintf(str, sizeof(str), &quot;0.%06u sec&quot;, (tick_interval_values[i]*10)%10);
    }</code></pre><p>But it does not work. Could you look and help me improve my code? I am begginer in this subject. I think that it would be helpful for many users.</p><p>Regards.</p></div><div id="comment-27969-info" class="comment-info"><span class="comment-age">(10 Dec '13, 04:03)</span> Yszty</div></div></div><div id="comment-tools-27772" class="comment-tools"></div><div class="clear"></div><div id="comment-27772-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

</div>

