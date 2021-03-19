+++
type = "question"
title = "how to replace &#x27;proto_tree_add_text&#x27; for wireshark 2.2"
description = '''Hello wireshark gurus,  I have a simple problem(but quite devastating for me). I am trying to update this dissector from wireshark 1.6 to 2.2 for windows. I have successfully removed all the errors due to change in API, except for one --&amp;gt; proto_tree_add_text. I know it should be replaced by proto...'''
date = "2016-12-02T09:20:00Z"
lastmod = "2016-12-02T10:15:00Z"
weight = 57793
keywords = [ "windows", "apichange", "proto_tree_add_text", "dissector", "plugin" ]
aliases = [ "/questions/57793" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [how to replace 'proto\_tree\_add\_text' for wireshark 2.2](/questions/57793/how-to-replace-proto_tree_add_text-for-wireshark-22)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57793-score" class="post-score" title="current number of votes">0</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hello wireshark gurus, I have a simple problem(but quite devastating for me). I am trying to update this dissector from wireshark 1.6 to 2.2 for windows. I have successfully removed all the errors due to change in API, except for one --&gt; proto_tree_add_text. I know it should be replaced by proto_tree_add_xxx. But I couldn't find any way of understanding how to implement the change.I have read the readme files. but I'm unable to attain any success after trying a lot. New functions require some parameter named 'id' eg. proto_tree_add_string(tree, id, tvb, start, length, value_ptr); What is this ID? Could anyone please guide me solving this issue. I'm posting some of the code snippets. Thanks</p><pre><code>proto_item *header_item = proto_tree_add_text(cidsifecmd_tree, tvb, CIDSIFE_HEADER_FIRST_BYTE_START, CIDSIFE_HEADER_LENGTH,
        &quot;Header &gt; Protocol Revision: %u, Airframe Manufacturer: %u, Data Length: %u&quot;,
        ife_protocol_revision, ife_airframe_manufactor, ife_data_length
);

proto_tree_add_text(command_tree, tvb,  7, 1, &quot;Direct PA:\t\t%s&quot;, try_val_to_str(getbits(tvb_get_guint8(tvb, 7), 1, 2), discrete_status_var));

proto_tree_add_text(command_tree, tvb, 7, 1, &quot;Video In Use:\t%s&quot;,
                try_val_to_str(getbits(tvb_get_guint8(tvb, 7), 3, 2), discrete_status_var)
        );
        proto_tree_add_text(command_tree, tvb, 5, 10, &quot;Item\tVPA\tNMPA\tAudioType&quot;);
        for (row = 0; row &lt; 10; row++) {
            proto_tree_add_text(command_tree, tvb, 5, 10, &quot;VPA%u\t%s\t%s\t%s&quot;,
                    row + 1,
                    try_val_to_str(pa_array[row][0], discrete_status_var),
                    try_val_to_str(pa_array[row][1], discrete_status_var),
                    try_val_to_str(pa_array[row][2], vpa_audio_type_var)
            );
        }

proto_tree_add_text(sub_tree, tvb, CIDSIFE_CMD42_FIRSTELEMENT_START + tmp_row * CIDSIFE_CMD42_ELEMENT_LENGTH, CIDSIFE_CMD42_ELEMENT_LENGTH, str);</code></pre><hr /><p>It also appears once in the header file</p><pre><code>#define PROTO_TREE_ADD_HEADER( ife_tree, ife_command, element_start, element_length )                       \
        proto_item *sub_item = proto_tree_add_text(      \
                (ife_tree) , tvb, (element_start),      \
                ife_numberOfElements * (element_length),  \
                &quot;%s (%u entries)&quot;,   \
                try_val_to_str( (ife_command) , command_name_var),  \
                ife_numberOfElements        \
        );       \
   proto_tree *sub_tree = proto_item_add_subtree(sub_item, ett_cidsifecmd_tree)</code></pre></div><div id="question-tags" class="tags-container tags">windows apichange proto_tree_add_text dissector plugin</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>02 Dec '16, 09:20</strong></p><img src="https://secure.gravatar.com/avatar/a908c48c60a3ba8f08a762a9cb58268f?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="xaheen&#39;s gravatar image" /><p>xaheen<br />
<span class="score" title="71 reputation points">71</span><span title="14 badges"><span class="badge1">●</span><span class="badgecount">14</span></span><span title="15 badges"><span class="silver">●</span><span class="badgecount">15</span></span><span title="19 badges"><span class="bronze">●</span><span class="badgecount">19</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="xaheen has one accepted answer">50%</span></p></div><div class="post-update-info post-update-info-edited"><p>edited 02 Dec '16, 10:05</p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span></p></div></div><div id="comments-container-57793" class="comments-container"></div><div id="comment-tools-57793" class="comment-tools"></div><div class="clear"></div><div id="comment-57793-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="57797"></span>

<div id="answer-container-57797" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-57797-score" class="post-score" title="current number of votes">1</div></div></td><td><div class="item-right"><div class="answer-body"><p>The is a Perl helper script in tools\convert_proto_tree_add_text.pl that does a fair bit of the donkey work for you, but may need manual assistance to complete the conversion.</p><p>The script might not work correctly on your macro in the header file, but after you see what the script has done to the other functions you should be able to work out what is needed in the macro. I suspect the macro may need additional parameter(s).</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>02 Dec '16, 10:15</strong></p><img src="https://secure.gravatar.com/avatar/d2a7e24ca66604c749c7c88c1da8ff78?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="grahamb&#39;s gravatar image" /><p>grahamb ♦<br />
<span class="score" title="19834 reputation points"><span>19.8k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="30 badges"><span class="silver">●</span><span class="badgecount">30</span></span><span title="206 badges"><span class="bronze">●</span><span class="badgecount">206</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="grahamb has 274 accepted answers">22%</span></p></div></div><div id="comments-container-57797" class="comments-container"><span id="57880"></span><div id="comment-57880" class="comment"><div id="post-57880-score" class="comment-score"></div><div class="comment-text"><p>Thanks a lot @grahamb Sadly now I am lost with this convert_proto_tree_add_text.pl file :p trying to figure out what to do with it as I have no Idea about Perl.</p></div><div id="comment-57880-info" class="comment-info"><span class="comment-age">(05 Dec '16, 13:58)</span> xaheen</div></div></div><div id="comment-tools-57797" class="comment-tools"></div><div class="clear"></div><div id="comment-57797-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</hr>

</div>

</div>

