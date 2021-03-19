+++
type = "question"
title = "Using two instances of a field as different custom columns"
description = '''Hi folks! What I want to do, is to add 2 custom columns to the WireShark view. The columns must contain a custom value which I add there by performing the following steps:  Choose the relevant packet Open the relevant layer (GSM Mobile Application in my case) Click right mouse button on the desired ...'''
date = "2012-03-25T05:10:00Z"
lastmod = "2012-03-25T07:17:00Z"
weight = 9742
keywords = [ "columns", "custom" ]
aliases = [ "/questions/9742" ]
osqa_answers = 0
osqa_accepted = true
+++

<div class="headNormal">

# [Using two instances of a field as different custom columns](/questions/9742/using-two-instances-of-a-field-as-different-custom-columns)

</div>

<div id="main-body">

<div id="askform">

<table id="question-table" style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9742-score" class="post-score" title="current number of votes">1</div><div id="favorite-count" class="favorite-count"></div></div></td><td><div id="item-right"><div class="question-body"><p>Hi folks!</p><p>What I want to do, is to add 2 custom columns to the WireShark view. The columns must contain a custom value which I add there by performing the following steps:</p><ol><li>Choose the relevant packet</li><li>Open the relevant layer (<em>GSM Mobile Application in my case</em>)</li><li>Click right mouse button on the desired field and choose "Apply as filter"<img src="https://osqa-ask.wireshark.org/upfiles/apply_as_filter_2.JPG" alt="alt text" /></li><li>Then I check what appear in the filter edit field and copy this value (in this case: <strong>gsm_map.address.digits</strong>) <img src="https://osqa-ask.wireshark.org/upfiles/filter_field.JPG" alt="List item" /></li><li>Then I go to <em>Edit-&gt;Preferences-&gt;Columns</em>. Click on "Add", choose "Custom" Field Type and then use the field name acquired in step 4 (<strong>gsm_map.address.digits</strong>)</li></ol><p>This way working fine, however a problem arise when I want to create 2 custom columns where the field name have the same name. For example consider the following screenshot: <img src="https://osqa-ask.wireshark.org/upfiles/screenshot_fields.JPG" alt="alt text" /></p><p>Here, I have 2 fields with similar name (<strong>gsm_map.address.digits</strong>). Obviously I cannot use the same name twice since it only will show the value which was assigned to the last appearing field.</p><p>Is there any way to solve this limitation?</p><p>Thanks!</p></div><div id="question-tags" class="tags-container tags">columns custom</div><div id="question-controls" class="post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>asked <strong>25 Mar '12, 05:10</strong></p><img src="https://secure.gravatar.com/avatar/aab36e75e2a1b09199da99501429f49e?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Eugene%20S&#39;s gravatar image" /><p>Eugene S<br />
<span class="score" title="21 reputation points">21</span><span title="2 badges"><span class="badge1">●</span><span class="badgecount">2</span></span><span title="2 badges"><span class="silver">●</span><span class="badgecount">2</span></span><span title="5 badges"><span class="bronze">●</span><span class="badgecount">5</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Eugene S has no accepted answers">0%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 25 Mar '12, 07:19</p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span></p></img></div></div><div id="comments-container-9742" class="comments-container"></div><div id="comment-tools-9742" class="comment-tools"></div><div class="clear"></div><div id="comment-9742-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

------------------------------------------------------------------------

<div class="tabBar">

<span id="sort-top"></span>

<div class="headQuestions">

One Answer:

</div>

</div>

<span id="9743"></span>

<div id="answer-container-9743" class="answer accepted-answer">

<table style="width:100%;"><colgroup><col style="width: 50%" /><col style="width: 50%" /></colgroup><tbody><tr class="odd"><td style="width: 30px; vertical-align: top"><div class="vote-buttons"><div id="post-9743-score" class="post-score" title="current number of votes">2</div></div></td><td><div class="item-right"><div class="answer-body"><p>You'd have to create two columns with different "Field occurrence" values - 1 for the first "Address digits" field, 2 for the second. The dialog that pops up for "Columns" in Edit-&gt;Preferences has, for custom columns, a "Field occurrence" field to the right of the "Field name" field. That's where you'd put the "Field occurrence" value.</p><p>If the dialog doesn't have that field, it might have been added in a later version of Wireshark than the one you're using, in which case you're out of luck.</p><p>(Unfortunately, there's no way to, for example, say "the occurrence of gsm_map.address.digits in the networkNode-Number tree" or something such as that. I suspect that's what you really want, rather than the first and second occurrences of the field.)</p></div><div class="answer-controls post-controls"></div><div class="post-update-info-container"><div class="post-update-info post-update-info-user"><p>answered <strong>25 Mar '12, 07:17</strong></p><img src="https://secure.gravatar.com/avatar/f93de7000747ab5efb5acd3034b2ebd7?s=32&amp;d=identicon&amp;r=g" class="gravatar" width="32" height="32" alt="Guy%20Harris&#39;s gravatar image" /><p>Guy Harris ♦♦<br />
<span class="score" title="17443 reputation points"><span>17.4k</span></span><span title="3 badges"><span class="badge1">●</span><span class="badgecount">3</span></span><span title="35 badges"><span class="silver">●</span><span class="badgecount">35</span></span><span title="196 badges"><span class="bronze">●</span><span class="badgecount">196</span></span><br />
<span class="accept_rate" title="Rate of the user&#39;s accepted answers">accept rate:</span> <span title="Guy Harris has 216 accepted answers">19%</span></p></img></div><div class="post-update-info post-update-info-edited"><p>edited 25 Mar '12, 11:51</p></div></div><div id="comments-container-9743" class="comments-container"><span id="9745"></span><div id="comment-9745" class="comment"><div id="post-9745-score" class="comment-score"></div><div class="comment-text"><p>@Guy Harris Thank you for your comment. However I'm not sure I understood your explanation. Could you please rephrase it? Thank you!</p></div><div id="comment-9745-info" class="comment-info"><span class="comment-age">(25 Mar '12, 07:50)</span> Eugene S</div></div><span id="9748"></span><div id="comment-9748" class="comment"><div id="post-9748-score" class="comment-score"></div><div class="comment-text"><p>OK, I've given more details.</p></div><div id="comment-9748-info" class="comment-info"><span class="comment-age">(25 Mar '12, 11:51)</span> Guy Harris ♦♦</div></div><span id="9750"></span><div id="comment-9750" class="comment"><div id="post-9750-score" class="comment-score"></div><div class="comment-text"><p>@Guy Harris You are right! I was using pretty old version of Wireshark. I just installed the last stable release (1.6.5) and now I can see the "Field Occurrence" you were referring to. Actually in this version both values already appeared in my custom created field by default. Thanks!</p></div><div id="comment-9750-info" class="comment-info"><span class="comment-age">(25 Mar '12, 14:42)</span> Eugene S</div></div><span id="9751"></span><div id="comment-9751" class="comment"><div id="post-9751-score" class="comment-score"></div><div class="comment-text"><p>In 1.6, if you don't specify an occurrence, it might show all occurrences (if that's what you mean by "both values already appeared in my custom created field by default").</p></div><div id="comment-9751-info" class="comment-info"><span class="comment-age">(25 Mar '12, 17:44)</span> Guy Harris ♦♦</div></div><span id="9755"></span><div id="comment-9755" class="comment"><div id="post-9755-score" class="comment-score"></div><div class="comment-text"><p>@Guy Harris Yes, that's exactly what I mean!</p></div><div id="comment-9755-info" class="comment-info"><span class="comment-age">(26 Mar '12, 00:44)</span> Eugene S</div></div></div><div id="comment-tools-9743" class="comment-tools"></div><div class="clear"></div><div id="comment-9743-form-container" class="comment-form-container"></div><div class="clear"></div></div></td></tr></tbody></table>

</div>

<div class="paginator-container-left">

</div>

</div>

</div>

