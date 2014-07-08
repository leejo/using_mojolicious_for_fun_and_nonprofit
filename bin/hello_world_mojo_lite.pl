#!/usr/bin/env perl

# automatically enables strict, warnings, utf8 and 5.10 features
use Mojolicious::Lite;
use Mojo::JSON;

any '/hello_world' => sub {
    my ( $self ) = @_;
    $self->render( text => "Bonjour à tous" );
};

post '/hello_to' => sub {
    my ( $self ) = @_;

    my $params = $self->req->json;

    $self->render(
        status => 200,
        json   => {
            hello    => $params->{who},
            complete => Mojo::JSON->true,
        },
    );
};

app->start;
