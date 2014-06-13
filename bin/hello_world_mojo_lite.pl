#!/usr/bin/env perl

# automatically enables strict, warnings, utf8 and 5.10 features
use Mojolicious::Lite;

any '/hello_world' => sub {
    my ( $self ) = @_;
    $self->render( text => "Bonjour à tous" );
};

app->start;
