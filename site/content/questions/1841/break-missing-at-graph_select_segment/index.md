+++
type = "question"
title = "break missing at graph_select_segment?"
description = '''It really does not make sense to me that a break is not present before case ELMT_ARC:  static void graph_select_segment (struct graph g, int x, int y) {  struct element_list list;  struct element *e;  guint num = 0; debug(DBS_FENTRY) puts (&quot;graph_select_segment()&quot;);  x -= g-&amp;gt;geom.x; y = g-&amp;gt;geo...'''
date = "2011-01-20T22:12:00Z"
lastmod = "2011-01-21T00:41:00Z"
weight = 1841
keywords = [ "development", "code" ]
aliases = [ "/questions/1841" ]
osqa_answers = 0
osqa_accepted = false
+++

<div class="headNormal">

# [break missing at graph\_select\_segment?](/questions/1841/break-missing-at-graph_select_segment)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1841-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>It really does not make sense to me that a break is not present before case ELMT_ARC: static void graph_select_segment (struct graph <em>g, int x, int y) { struct element_list</em> list; struct element *e; guint num = 0;</p><pre><code>debug(DBS_FENTRY) puts (&quot;graph_select_segment()&quot;);

x -= g-&gt;geom.x;
y = g-&gt;geom.height-1 - (y - g-&gt;geom.y);

set_busy_cursor (g-&gt;drawing_area-&gt;window);

for (list=g-&gt;elists; list; list=list-&gt;next)
    for (e=list-&gt;elements; e-&gt;type != ELMT_NONE; e++) {
        switch (e-&gt;type) {
        case ELMT_RECT:
            break;
        case ELMT_LINE:
            if (line_detect_collision (e, x, y)) {
                num = e-&gt;parent-&gt;num;
            }
        case ELMT_ARC:
            if (arc_detect_collision (e, x, y)) {
                num = e-&gt;parent-&gt;num;
            }
            break;
        default:
            break;
        }
    }

if (num) {
    cf_goto_frame(&amp;cfile, num);
}
unset_busy_cursor (g-&gt;drawing_area-&gt;window);</code></pre><p>}</p></div><div id="question-tags" class="tags-container tags">development code</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>20 Jan '11, 22:12</strong></p><img src="https://secure.gravatar.com/avatar/01ad5b8c718dd2465bc28a9d15661152?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="billyjeans&#39;s gravatar image" /><p>billyjeans<br />
<span class="score" title="1 reputation points">1</span><span title="1 badges"><span class="badge1">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="silver">●</span><span class="badgecount">1</span></span><span title="1 badges"><span class="bronze">●</span><span class="badgecount">1</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="billyjeans has no accepted answers">0%</span></p></div></div><div id="comments-container-1841" class="comments-container"></div><div id="comment-tools-1841" class="comment-tools"></div><div class="clear"></div><div id="comment-1841-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="1845"></span>

<div id="answer-container-1845" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-1845-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>It's better to file complete bug reports in the <a href="https://bugs.wireshark.org">bug database</a>, i.s.o. sending us on a wild goose chase. You didn't specify which version of the source code you're referring to, or which file.</p><p>Eventually I found the offending code. It doesn't have consequences, but in the name of purity it's cleaned up.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Jan '11, 00:41</strong></p><img src="https://secure.gravatar.com/avatar/2337f0406681e5c72ea0e6f1f0d6c0b0?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Jaap&#39;s gravatar image" /><p>Jaap ♦<br />
<span class="score" title="11680 reputation points"><span>11.7k</span></span><span title="16 badges"><span class="silver">●</span><span class="badgecount">16</span></span><span title="101 badges"><span class="bronze">●</span><span class="badgecount">101</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Jaap has 155 accepted answers">14%</span></p></div></div><div id="comments-container-1845" class="comments-container"></div><div id="comment-tools-1845" class="comment-tools"></div><div class="clear"></div><div id="comment-1845-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

