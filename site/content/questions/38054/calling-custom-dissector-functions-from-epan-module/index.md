+++
type = "question"
title = "calling custom dissector functions from epan module"
description = '''Hi all I have developed a custom dissector module, which is included in plugins folder of the wireshark. I have a requirement that when plugins get register need to create a data structure to store data required for dissection. This data structure need to be present through out the life time of the ...'''
date = "2014-11-21T13:23:00Z"
lastmod = "2014-11-21T14:33:00Z"
weight = 38054
keywords = [ "cleanup", "epan", "linking-modules" ]
aliases = [ "/questions/38054" ]
osqa_answers = 2
osqa_accepted = true
+++

<div class="headNormal">

# [calling custom dissector functions from epan module](/questions/38054/calling-custom-dissector-functions-from-epan-module)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38054-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi all</p><p>I have developed a custom dissector module, which is included in plugins folder of the wireshark. I have a requirement that when plugins get register need to create a data structure to store data required for dissection. This data structure need to be present through out the life time of the Wireshark process. But, when Wireshark is quit/closed need to cleanup this data structure. For doing this i have written a cleanup function, but not sure where to call this function from. After exploring i tried invoking this function from epan module, epan_cleanup() function in epan.c.</p><p>But, faced issue in invoking this function from epan module as the objects are not linked. Then i modified the makefile of epan directory to include the .lo file of my custom dissector and invoke this function. Both, compilation and linking went fine, but, when i execute the Wireshark, the custom cleanup function is invoked but the data structure memory reference is not correct.</p><p>Sample code:</p><pre><code>In custom_dissector.c

typedef struct xyz{
int a;
char *name;
int b;
}XYZ;

XYZ proto_names[100]; // Global

void custom_cleanup()
{
    int i;
    for (i=0;i&lt;100;i++)
    {
        if (XYZ.name != NULL)
        {
            free (XYZ.name);
        }
    }
}

in epan.c file :
void epan_cleanup()
{
....
....
...
custom_cleanup(); // could not properly reference XYZ memory
}</code></pre><p>Would like know the following, - Which is the right place to invoke custom cleanup functions during wireshark exit. - How to link custom cleanup function in plugin folder and epan module.</p><p>Request your help on the same. Thank you Kiran Kumar G</p></div><div id="question-tags" class="tags-container tags">cleanup epan linking-modules</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>21 Nov '14, 13:23</strong></p><img src="https://secure.gravatar.com/avatar/ae4b5aebc9d00c273018cc64d3ac583a?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Kiran%20Kumar%20G&#39;s gravatar image" /><p>Kiran Kumar G<br />
<span class="score" title="21 reputation points">21</span><span title="11 badges"><span class="badge1">●</span><span class="badgecount">11</span></span><span title="14 badges"><span class="silver">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="bronze">●</span><span class="badgecount">15</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Kiran Kumar G has no accepted answers">0%</span></p></div></div><div id="comments-container-38054" class="comments-container"></div><div id="comment-tools-38054" class="comment-tools"></div><div class="clear"></div><div id="comment-38054-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

2 Answers:

</div>

</div>

<span id="38057"></span>

<div id="answer-container-38057" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38057-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>If you only need to cleanup a memory allocation, I wouldn't worry too much, the OS will clean that all up as the Wireshark process exits.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '14, 14:33</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-38057" class="comments-container"></div><div id="comment-tools-38057" class="comment-tools"></div><div class="clear"></div><div id="comment-38057-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<span id="38056"></span>

<div id="answer-container-38056" class="answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-38056-score" class="post-score" title="current number of votes">0</div></div></td><td><div class="item-right"><div class="answer-body"><p>Why not simply allocate your memory with wmem based functions and the epan scope, like for example wmem_alloc(wmem_epan_scope(), size)? Wireshark will automatically release the memory for you when closed.</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>21 Nov '14, 14:32</strong></p><img src="https://secure.gravatar.com/avatar/713f24fd877861260b71ecd455018625?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Pascal%20Quantin&#39;s gravatar image" /><p>Pascal Quantin<br />
<span class="score" title="5544 reputation points"><span>5.5k</span></span><span title="10 badges"><span class="silver">●</span><span class="badgecount">10</span></span><span title="60 badges"><span class="bronze">●</span><span class="badgecount">60</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Pascal Quantin has 92 accepted answers">30%</span></p></div></div><div id="comments-container-38056" class="comments-container"></div><div id="comment-tools-38056" class="comment-tools"></div><div class="clear"></div><div id="comment-38056-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

